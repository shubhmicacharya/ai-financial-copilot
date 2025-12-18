def generate_insights(summary):
    return f"""
    You spent a total of ₹{summary['total_spent']}.
    Most of your expenses were in {summary['top_category']}.
    Consider optimizing discretionary spending.
    """
