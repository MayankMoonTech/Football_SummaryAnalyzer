def build_prompt(metrics):

    prompt = f"""
You are a professional football tactical analyst.

Match Statistics:

Total Passes: {metrics['total_passes']}
Shots: {metrics['shots']}
Tackles: {metrics['tackles']}
Pass Accuracy: {metrics['pass_accuracy']}

Provide tactical insights including:

1. Attacking performance
2. Defensive performance
3. Tactical patterns
4. Improvement suggestions
"""

    return prompt