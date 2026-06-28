# ai_core/optimized_ai_engine.py

#THRESHOLDS = {
#    "selected": 60,
#    "hold": 58
#}


#def adjust_decision(score, technical, integrity_risk):

    #### False Positive Prevention
 #   if score > 80 and integrity_risk == "High Risk":
 #       return "Hold / Review"

    ### False Negative Prevention
    #if score < 60 and technical > 85:
     #   return "Hold / Review"

    ### Normal Logic
    #if score >= THRESHOLDS["selected"]:
     #   return "Selected"

    #elif score >= THRESHOLDS["hold"]:
     #   return "Hold / Review"

    #return "Rejected"
def adjust_decision(score, technical, integrity_risk):

    if score >= 60:
        return "Selected"
    else:
        return "Rejected"