#! python
# -*- coding:utf-8 -*-
#
# www.twilio.com //mutou110414twilio
#
from twilio.rest import Client
accountSID = 'AC5e2b374dfa2a5c9f66a6443034ba82c2'
authToken = '014a3718b01899b1da065a771290e0b9'

twlioClient = Client(accountSID,authToken)

myTwilioNumber = '+15032105142'
toCellPhone = '+8613430983889'

message = twlioClient.messages.create(body = 'Second message from twilio-Trilnumber:hello man .',from_=myTwilioNumber,to=toCellPhone)

# cannot receive the SMS TODAY(2019-02-08)
#
