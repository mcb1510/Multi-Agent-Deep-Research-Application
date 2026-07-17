from agents import Agent, ModelSettings, function_tool, Runner
from messenger import send_email as send_email_raw
from writer_agent import ReportData
from dotenv import load_dotenv

load_dotenv(override=True)
MODEL_NAME = "gpt-5.4-mini"
settings = ModelSettings(tool_choice="required")
@function_tool
def send_email_tool(subject:str, text_body:str, html_body:str) -> str:
    """
    Send out an email with the given subject and body to all sales prospects

    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
    """

    send_email_raw(subject, text_body, html_body)
    return "Email sent successfully"

INSTRUCTIONS ="""
You are provided with a detailed report. Use your tool to send an email, converting the report into a clean, well presented HTML email with an
appropriate subject line.
"""
email_agent = Agent(name="Email Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, tools=[send_email_tool], model_settings=settings)


async def send_email(report:ReportData) -> None:
    await Runner.run(email_agent, report.markdown_report)