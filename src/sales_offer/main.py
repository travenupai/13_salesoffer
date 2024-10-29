#!/usr/bin/env python
import sys

from sales_offer.crew import SalesOfferCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "customer_info": {
            "name": "CrewAI",
            "industry": "Agentes Inteligenes",
            "size": "50-100 employees",
            "current_challenges": "Growth and Scale",
            "budget_range": "50000-1000000",
        },
        "company_info": {
            "name": "TravenUp",
            "products": ["Travel Experiences", "Travel Assistance"],
            "pricing_models": [
                "Modelo de Preço Básico",
                "Modelo de Preço Premium",
            ],
            "unique_selling_points": ["Suporte 24/7", "Personalização Completa"],
        },
    }
    SalesOfferCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SalesOfferCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SalesOfferCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SalesOfferCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
