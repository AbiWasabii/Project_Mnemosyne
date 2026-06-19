from services.agents.daily_journal_agent import create_daily_journal


journal = create_daily_journal(
    owner="Alex"
)

print(journal)