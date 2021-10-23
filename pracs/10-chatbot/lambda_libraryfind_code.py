import json
import math
import dateutil.parser
import datetime
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """

# extracts slots from the intent request
def get_slots(intent_request):
    return intent_request['currentIntent']['slots']

# returns the response to the bot
def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response

""" --- Helper Functions --- """
def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float('nan')


def build_validation_result(is_valid, violated_slot, message_content):
    if message_content is None:
        return {
            "isValid": is_valid,
            "violatedSlot": violated_slot,
        }

    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }


def isvalid_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except ValueError:
        return False

# checks whether the library has staff in attendance at the current time
def check_library_service(intent_request):
    now = datetime.datetime.now()
    current_hour = now.hour
    current_day = now.weekday()
    logger.debug('hour={} day={}'.format(current_hour, current_day))
    if current_day < 5:
        if current_hour > 18 and current_hour < 8:
            output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
            output_session_attributes['libraryservice'] = False
            return False
    elif current_hour < 12 and current_hour > 17:
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        output_session_attributes['libraryservice'] = False
        return False
    else:
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        output_session_attributes['libraryservice'] = True
        return True
    

""" --- Main Response Control --- """

# identifies what people are trying to find and selects the correct response
def find_something(intent_request):
    # you will need to add more bathroom and copier words
    # people also use copiers for printing
    bathroom_words = ['bathroom', 'toilet']
    copier_words = ['the photocopier', 'photocopiers', 'scanner', 'scanners']
    # add kitchen_words here
    
    thing_to_find = get_slots(intent_request)["foleyb_things"]
    source = intent_request['invocationSource']
    
    #response if the person is looking for the toilet
    if thing_to_find is not None and thing_to_find.lower() in bathroom_words:
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        output_session_attributes['enquirytype'] = 'findBathroom'
        output_session_attributes['robotaction'] = 'guideright'
        return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'The {} is located to my right hand side just near the lifts'.format(thing_to_find)})
    
    # response if the person is looking for a photocopier
    if thing_to_find is not None and thing_to_find.lower() in copier_words:
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        output_session_attributes['enquirytype'] = 'findCopier'
        output_session_attributes['robotaction'] = 'guideright'
        return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'If you go straight from my right hand side, the nearest {} is about 50 meters away and there are more up the stairs in Duhig Tower'.format(thing_to_find)})
    
    #add here the if statement for finding the kitchen
    '''
        use these options
        output_session_attributes['enquirytype'] = 'findKitchen'
        output_session_attributes['robotaction'] = 'talk7'
    '''
    
    # default response if the thing to be found is not identified
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    output_session_attributes['enquirytype'] = 'findUnknown'
    output_session_attributes['robotaction'] = 'zhua'
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Sorry but I do not know where {} is located'.format(thing_to_find)})


""" --- Intents --- """

def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    # Set library open flag
    library_service_available = check_library_service(intent_request)

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'foley_findLibraryResource':
        return find_something(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """

def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    
    # By default, treat the user request as coming from the Australia/Brisbane time zone.
    os.environ['TZ'] = 'Australia/Brisbane'
    time.tzset()
    
    # log the bot name
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)