## Decisions

- De gebruiker moet zelf de inspecteurs, bedrijven en bezoekrapporten inlezen.
- Er is gekozen om de print statements waar de gebruiker mee interacteerd (front-end) voor deze applicatie niet los te koppelen van de logica aangezien de applicatie overzichtelijk genoeg is voor de functionaliteit dat het heeft.

## Vragen

- Wat wordt er bedoelt met de totale uitstoot CO2-equivalent? (is dat de totale_berekening van alle verschillende gas uitstoten bij elkaar?)

## Todo

- bezoekrapporten inlezen

-

## Problems

- Er is geen check of er al een inspecteur met dezelfde code is ingelezen.

## Installation and Setup Instructions

Prerequisites:
Ensure you have Python installed on your system.

Clone the Repository:
First, clone the repository to your local machine:

```
git clone https://github.com/yannicklansink/Uitstoot-monitoring-schone-lucht-bv
```

Set Up a Virtual Environment to avoid potential version issues.

Create a virtual environment:

```
python -m venv myenv
```

Activate the virtual environment:

```
.\myenv\Scripts\activate
```

macOS and Linux:

Install Dependencies:
With the virtual environment activated, install the required packages:

```
pip install -r requirements.txt
```

Running the Project:

```
python module.menu.py
```
