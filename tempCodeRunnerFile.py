
# def hello_world():
#     now = datetime.utcnow()
#     customerId = request.args.get("customerId")
#     eventMessage = request.args.get("eventMessage")

#     transaction_data = {
#         "customerId": customerId,
#         "eventMessage": eventMessage,
#         "time": {
#             "year": now.year,
#             "month": now.month,
#             "day": now.day,
#             "hour": now.hour,
#             "minute": now.minute,
#             "second": now.second,
#             "microsecond": now.microsecond
#         }
#     }

#     collection.insert_one(transaction_data)
#     return "True"
