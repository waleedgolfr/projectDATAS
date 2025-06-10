import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import requests
from bs4 import BeautifulSoup

# Set Seaborn style and color palette
sns.set(style="whitegrid")
colors = ["purple", "yellow"]

# 1. Load the dataset (change the path accordingly)
df = pd.read_csv("C:\\Users\\user\\Desktop\\titanic\\titanic_1.csv")

# 2. Clean the data
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# 3. Save the first 5 rows to a JSON file
first_5 = df.head(5)
first_5_json = first_5.to_dict(orient="records")
with open("first_5_rows.json", "w") as f:
    json.dump(first_5_json, f, indent=4)
print("✅ Saved first 5 rows to 'first_5_rows.json'")

# 4. Create multiple charts

# Chart 1: Survivors by Gender
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Sex", hue="Survived", palette=colors)
plt.title("Survivors by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.savefig("chart1_gender_survival.png")
plt.show()

# Chart 2: Survivors by Age
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", hue="Survived", multiple="stack", palette=colors, bins=30)
plt.title("Survivors by Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.savefig("chart2_age_survival.png")
plt.show()

# Chart 3: Fare by Passenger Class
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Pclass", y="Fare", palette=colors)
plt.title("Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.savefig("chart3_fare_pclass.png")
plt.show()

# Chart 4: Survivors by Embarkation Port
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Embarked", hue="Survived", palette=colors)
plt.title("Survivors by Embarkation Port")
plt.xlabel("Embarkation Port")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.savefig("chart4_embarked_survival.png")
plt.show()

# 5. Web scraping Wikipedia Titanic summary (first 5 paragraphs)
url = "https://en.wikipedia.org/wiki/Titanic"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract first 5 paragraphs of the main content (skip empty or irrelevant ones)
paragraphs = []
for p in soup.find_all("p"):
    text = p.get_text().strip()
    if len(text) > 50:
        paragraphs.append(text)
    if len(paragraphs) == 5:
        break

wiki_summary = "\n\n".join(paragraphs)

# Print summary in terminal
print("\n📖 Titanic - Wikipedia Summary:\n")
print(wiki_summary)

# Save summary to a text file
with open("titanic_summary.txt", "w", encoding="utf-8") as f:
    f.write(wiki_summary)

print("\n✅ Wikipedia summary saved to 'titanic_summary.txt'")
