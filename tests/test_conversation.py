from screening_ai.conversation_engine import ConversationStateMachine

def test_flow():

    flow = {
        "start": "Q1",
        "nodes": {
            "Q1": {
                "question": "Test",
                "next": "END"
            }
        }
    }

    engine = ConversationStateMachine(flow)

    assert engine.get_question() == "Test"