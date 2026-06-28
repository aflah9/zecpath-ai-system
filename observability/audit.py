from datetime import datetime

def audit_log(action,user,candidate_id):

    return {

        "action":action,

        "user":user,

        "candidate_id":candidate_id,

        "timestamp":datetime.utcnow().isoformat()

    }