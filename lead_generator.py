from faker import Faker
import random

fake = Faker()

industries = ['SaaS', 'E-commerce', 'Fintech', 'Healthcare', 'Education']
channels = ['Website Demo Request', 'Email Campaign', 'LinkedIn Message', 'Referral', 'Organic Search']

def generate_lead():
    return {
        "name": fake.name(),
        "email": fake.company_email(),
        "company": fake.company(),
        "title": fake.job(),
        "inquiry_message": fake.sentence(nb_words=12),
        "source_channel": random.choice(channels),
        "industry": random.choice(industries)
    }