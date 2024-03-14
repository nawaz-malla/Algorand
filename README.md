# Algorand
blockchain
# commands 
# List of accounts 
1. algokit goal account list
# create app
2.$ algokit goal app create --creator 2BAXUCF4FSUHL7OI6GOR26MNYUSKFVQHSX2NZ5IGRD3XH6EKMKNLPCFXTA  --approval-prog approval.teal --clear-prog clear.teal --global-byteslices 8 --global-ints 8 --local-byteslices 8  --local-ints 8 
# optin 
3.$ algokit goal app optin  --app-id [ID-of-Contract] --from [ADDRESS]
# app call
4.$ algokit goal app call --app-id 1 --app-arg "str:myparam"  --from [ADDRESS]
# update app
5.algokit goal app update --app-id=[APPID] --from [ADDRESS]  --approval-prog [new_approval_program.teal]   --clear-prog [new_clear_state_program.teal]
# foreign app
$ algokit goal app call --foreign-app APP1ID --foreign-app APP2ID
# box method 
goal app method --app-id=53 --method="add_member2()void" --box="53,str:BoxA" --from=CONP4XZSXVZYA7PGYH7426OCAROGQPBTWBUD2334KPEAZIHY7ZRR653AFY
# reading contract state
$ goal app read --app-id 1 --guess-format --global --from [ADDRESS]
# app info
goal app info --app-id 1014