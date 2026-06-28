from ai_core.stable_system import stable_pipeline

from api.stable_api import api_response

from utils.error_handler import safe_execute


scores={

"ats":120,

"screening":70,

"technical":85,

"machine":65,

"hr":80

}


result=safe_execute(

lambda: stable_pipeline(

"C1001",

scores

)

)

print(

api_response(

True,

result

)

)