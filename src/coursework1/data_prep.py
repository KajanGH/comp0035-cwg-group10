from pathlib import Path
import pandas as pd

#FILE IMPORT SECTION-------------------------------
#imports all files that need to be prepped

current_directory = Path(__file__).resolve().parent
ctry = current_directory.parent.parent / "assigneddata" / "gp_sya_ctry.csv"
rgn = current_directory.parent.parent / "assigneddata" / "gp_sya_rgn.csv"
itl = current_directory.parent.parent / "assigneddata" / "gp_sya_itl.csv"
lad = current_directory.parent.parent / "assigneddata" / "gp_sya_lad.csv"

df_ctry = pd.read_csv(ctry)
df_rgn = pd.read_csv(rgn)
df_itl = pd.read_csv(itl)
df_lad = pd.read_csv(lad)
#DICTIONARY SECTION-------------------------------

#Region dictionary for the itl file
region_mapping = {
    'Bedfordshire and Hertfordshire': 'East of England',
    'East Anglia': 'East of England',
    'Essex': 'East of England',
    'Derbyshire and Nottinghamshire': 'East Midlands',
    'Leicestershire, Rutland and Northamptonshire': 'East Midlands',
    'Lincolnshire': 'East Midlands',
    'Northumberland, and Tyne and Wear': 'North East',
    'Tees Valley and Durham': 'North East',
    'Cheshire': 'North West',
    'Cumbria': 'North West',
    'Greater Manchester': 'North West',
    'Lancashire': 'North West',
    'Merseyside': 'North West',
    'Berkshire, Buckinghamshire and Oxfordshire': 'South East',
    'Hampshire and Isle of Wight': 'South East',
    'Kent': 'South East',
    'Surrey, East and West Sussex': 'South East',
    'Cornwall and Isles of Scilly': 'South West',
    'Devon': 'South West',
    'Dorset and Somerset': 'South West',
    'Gloucestershire, Wiltshire and Bath/Bristol area': 'South West',
    'Herefordshire, Worcestershire and Warwickshire': 'West Midlands',
    'Shropshire and Staffordshire': 'West Midlands',
    'West Midlands': 'West Midlands',
    'East Yorkshire and Northern Lincolnshire': 'Yorkshire and the Humber',
    'North Yorkshire': 'Yorkshire and the Humber',
    'South Yorkshire': 'Yorkshire and the Humber',
    'West Yorkshire': 'Yorkshire and the Humber',
    'Inner London - East': 'London',
    'Inner London - West': 'London',
    'Outer London - East and North East': 'London',
    'Outer London - South': 'London',
    'Outer London - West and North West': 'London'
}


#full location data dictionary for the lad file 

location_data = {
    "Bedford": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Central Bedfordshire": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Dacorum": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "East Hertfordshire": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Hertsmere": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Luton": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "North Hertfordshire": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "St Albans": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Stevenage": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Three Rivers": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Watford": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Welwyn Hatfield": {"Country": "England", "Region": "East of England", "ITL 2": "Bedfordshire and Hertfordshire"},
    "Babergh": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Breckland": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Broadland": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Cambridge": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "East Cambridgeshire": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "East Suffolk": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Fenland": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Great Yarmouth": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Huntingdonshire": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Ipswich": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "King's Lynn and West Norfolk": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Mid Suffolk": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "North Norfolk": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Norwich": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Peterborough": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "South Cambridgeshire": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "South Norfolk": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "West Suffolk": {"Country": "England", "Region": "East of England", "ITL 2": "East Anglia"},
    "Basildon": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Braintree": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Brentwood": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Broxbourne": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Castle Point": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Chelmsford": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Colchester": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Epping Forest": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Harlow": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Maldon": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Rochford": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Southend-on-Sea": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Tendring": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Thurrock": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Uttlesford": {"Country": "England", "Region": "East of England", "ITL 2": "Essex"},
    "Amber Valley": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Ashfield": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Bassetlaw": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Bolsover": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Broxtowe": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Chesterfield": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Derby": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Derbyshire Dales": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Erewash": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Gedling": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "High Peak": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Mansfield": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Newark and Sherwood": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "North East Derbyshire": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Nottingham": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Rushcliffe": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "South Derbyshire": {"Country": "England", "Region": "East Midlands", "ITL 2": "Derbyshire and Nottinghamshire"},
    "Blaby": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Charnwood": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Harborough": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Hinckley and Bosworth": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Leicester": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Melton": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "North West Leicestershire": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "North Northamptonshire": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Oadby and Wigston": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Rutland": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "West Northamptonshire": {"Country": "England", "Region": "East Midlands", "ITL 2": "Leicestershire, Rutland and Northamptonshire"},
    "Boston": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    "East Lindsey": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    "Lincoln": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    "North Kesteven": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    "South Holland": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    "South Kesteven": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    "West Lindsey": {"Country": "England", "Region": "East Midlands", "ITL 2": "Lincolnshire"},
    'Gateshead': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Northumberland, and Tyne and Wear'},
    'Newcastle upon Tyne': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Northumberland, and Tyne and Wear'},
    'North Tyneside': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Northumberland, and Tyne and Wear'},
    'Northumberland': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Northumberland, and Tyne and Wear'},
    'South Tyneside': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Northumberland, and Tyne and Wear'},
    'Sunderland': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Northumberland, and Tyne and Wear'},
    'County Durham': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Tees Valley and Durham'},
    'Darlington': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Tees Valley and Durham'},
    'Hartlepool': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Tees Valley and Durham'},
    'Middlesbrough': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Tees Valley and Durham'},
    'Redcar and Cleveland': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Tees Valley and Durham'},
    'Stockton-on-Tees': {'Country': 'England', 'Region': 'North East', 'ITL 2': 'Tees Valley and Durham'},
    'Cheshire East': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cheshire'},
    'Cheshire West and Chester': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cheshire'},
    'Halton': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cheshire'},
    'Warrington': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cheshire'},
    'Allerdale': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cumbria'},
    'Barrow-in-Furness': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cumbria'},
    'Carlisle': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cumbria'},
    'Copeland': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cumbria'},
    'Eden': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cumbria'},
    'South Lakeland': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Cumbria'},
    'Bolton': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Bury': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Manchester': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Oldham': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Rochdale': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Salford': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Stockport': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Tameside': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Trafford': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Wigan': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Greater Manchester'},
    'Blackburn with Darwen': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Blackpool': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Burnley': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Chorley': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Fylde': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Hyndburn': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Lancaster': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Pendle': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Preston': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Ribble Valley': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Rossendale': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'South Ribble': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'West Lancashire': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Wyre': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Lancashire'},
    'Knowsley': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Merseyside'},
    'Liverpool': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Merseyside'},
    'Sefton': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Merseyside'},
    'St. Helens': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Merseyside'},
    'Wirral': {'Country': 'England', 'Region': 'North West', 'ITL 2': 'Merseyside'},
    'Bracknell Forest': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Buckinghamshire': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Cherwell': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Milton Keynes': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Oxford': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Reading': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Slough': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'South Oxfordshire': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Vale of White Horse': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'West Berkshire': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'West Oxfordshire': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Windsor and Maidenhead': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Wokingham': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Berkshire, Buckinghamshire and Oxfordshire'},
    'Basingstoke and Deane': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'East Hampshire': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Eastleigh': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Fareham': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Gosport': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Hart': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Havant': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Isle of Wight': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'New Forest': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Portsmouth': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Rushmoor': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Southampton': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Test Valley': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Winchester': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Hampshire and Isle of Wight'},
    'Ashford': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Canterbury': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Dartford': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Dover': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Folkestone and Hythe': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Gravesham': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Maidstone': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Medway': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Sevenoaks': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Swale': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Thanet': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Tonbridge and Malling': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Tunbridge Wells': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Kent'},
    'Adur': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Arun': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Brighton and Hove': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Chichester': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Crawley': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Eastbourne': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Elmbridge': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Epsom and Ewell': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Guildford': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Hastings': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Horsham': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Lewes': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Mid Sussex': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Mole Valley': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Reigate and Banstead': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Rother': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Runnymede': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Spelthorne': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Surrey Heath': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Tandridge': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Waverley': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Wealden': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Woking': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    'Worthing': {'Country': 'England', 'Region': 'South East', 'ITL 2': 'Surrey, East and West Sussex'},
    "Cornwall": {"Country": "England", "Region": "South West", "ITL 2": "Cornwall and Isles of Scilly"},
    "Isles of Scilly": {"Country": "England", "Region": "South West", "ITL 2": "Cornwall and Isles of Scilly"},
    "East Devon": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Exeter": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Mid Devon": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "North Devon": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Plymouth": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "South Hams": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Teignbridge": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Torbay": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Torridge": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "West Devon": {"Country": "England", "Region": "South West", "ITL 2": "Devon"},
    "Bournemouth, Christchurch and Poole": {"Country": "England", "Region": "South West", "ITL 2": "Dorset and Somerset"},
    "Dorset": {"Country": "England", "Region": "South West", "ITL 2": "Dorset and Somerset"},
    "Mendip": {"Country": "England", "Region": "South West", "ITL 2": "Dorset and Somerset"},
    "Sedgemoor": {"Country": "England", "Region": "South West", "ITL 2": "Dorset and Somerset"},
    "Somerset West and Taunton": {"Country": "England", "Region": "South West", "ITL 2": "Dorset and Somerset"},
    "South Somerset": {"Country": "England", "Region": "South West", "ITL 2": "Dorset and Somerset"},
    "Bath and North East Somerset": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Bristol, City of": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Cheltenham": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Cotswold": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Forest of Dean": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Gloucester": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "North Somerset": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "South Gloucestershire": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Stroud": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Swindon": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Tewkesbury": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Wiltshire": {"Country": "England", "Region": "South West", "ITL 2": "Gloucestershire, Wiltshire and Bath/Bristol area"},
    "Bromsgrove": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Herefordshire, County of": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Malvern Hills": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "North Warwickshire": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Nuneaton and Bedworth": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Redditch": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Rugby": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Stratford-on-Avon": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Warwick": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Worcester": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Wychavon": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Wyre Forest": {"Country": "England", "Region": "West Midlands", "ITL 2": "Herefordshire, Worcestershire and Warwickshire"},
    "Cannock Chase": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "East Staffordshire": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Lichfield": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Newcastle-under-Lyme": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Shropshire": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "South Staffordshire": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Stafford": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Staffordshire Moorlands": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Stoke-on-Trent": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Tamworth": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Telford and Wrekin": {"Country": "England", "Region": "West Midlands", "ITL 2": "Shropshire and Staffordshire"},
    "Birmingham": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "Coventry": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "Dudley": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "Sandwell": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "Solihull": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "Walsall": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "Wolverhampton": {"Country": "England", "Region": "West Midlands", "ITL 2": "West Midlands"},
    "East Riding of Yorkshire": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "East Yorkshire and Northern Lincolnshire"},
    "Kingston upon Hull, City of": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "East Yorkshire and Northern Lincolnshire"},
    "North East Lincolnshire": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "East Yorkshire and Northern Lincolnshire"},
    "North Lincolnshire": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "East Yorkshire and Northern Lincolnshire"},
    "Craven": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Hambleton": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Harrogate": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Richmondshire": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Ryedale": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Scarborough": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Selby": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "York": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "North Yorkshire"},
    "Barnsley": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "South Yorkshire"},
    "Doncaster": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "South Yorkshire"},
    "Rotherham": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "South Yorkshire"},
    "Sheffield": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "South Yorkshire"},
    "Bradford": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "West Yorkshire"},
    "Calderdale": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "West Yorkshire"},
    "Kirklees": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "West Yorkshire"},
    "Leeds": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "West Yorkshire"},
    "Wakefield": {"Country": "England", "Region": "Yorkshire and the Humber", "ITL 2": "West Yorkshire"},
    "Hackney": {"Country": "England", "Region": "London", "ITL 2": "Inner London - East"},
    "Lewisham": {"Country": "England", "Region": "London", "ITL 2": "Inner London - East"},
    "Southwark": {"Country": "England", "Region": "London", "ITL 2": "Inner London - East"},
    "Tower Hamlets": {"Country": "England", "Region": "London", "ITL 2": "Inner London - East"},
    "Camden": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "City of London": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Hammersmith and Fulham": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Islington": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Kensington and Chelsea": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Lambeth": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Wandsworth": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Westminster": {"Country": "England", "Region": "London", "ITL 2": "Inner London - West"},
    "Barking and Dagenham": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Bexley": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Enfield": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Greenwich": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Haringey": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Havering": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Newham": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Redbridge": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Waltham Forest": {"Country": "England", "Region": "London", "ITL 2": "Outer London - East and North East"},
    "Bromley": {"Country": "England", "Region": "London", "ITL 2": "Outer London - South"},
    "Croydon": {"Country": "England", "Region": "London", "ITL 2": "Outer London - South"},
    "Kingston upon Thames": {"Country": "England", "Region": "London", "ITL 2": "Outer London - South"},
    "Merton": {"Country": "England", "Region": "London", "ITL 2": "Outer London - South"},
    "Richmond upon Thames": {"Country": "England", "Region": "London", "ITL 2": "Outer London - South"},
    "Sutton": {"Country": "England", "Region": "London", "ITL 2": "Outer London - South"},
    "Barnet": {"Country": "England", "Region": "London", "ITL 2": "Outer London - West and North West"},
    "Brent": {"Country": "England", "Region": "London", "ITL 2": "Outer London - West and North West"},
    "Ealing": {"Country": "England", "Region": "London", "ITL 2": "Outer London - West and North West"},
    "Harrow": {"Country": "England", "Region": "London", "ITL 2": "Outer London - West and North West"},
    "Hillingdon": {"Country": "England", "Region": "London", "ITL 2": "Outer London - West and North West"},
    "Hounslow": {"Country": "England", "Region": "London", "ITL 2": "Outer London - West and North West"},

}

longlat = {'Amber Valley': {'Latitude': 53.0290384, 'Longitude': -1.46250311}, 'Ashfield': {'Latitude': 53.08977375, 'Longitude': -1.251876746}, 'Bassetlaw': {'Latitude': 53.34945205, 'Longitude': -0.961660401}, 'Bolsover': {'Latitude': 53.228666, 'Longitude': -1.2912756}, 'Broxtowe': {'Latitude': 52.9782566, 'Longitude': -1.2170642}, 'Chesterfield': {'Latitude': 53.2352134, 'Longitude': -1.4264097}, 'Derby': {'Latitude': 52.9212617, 'Longitude': -1.4761491}, 'Derbyshire Dales': {'Latitude': 53.1302876, 'Longitude': -1.656173279}, 'Erewash': {'Latitude': 52.93800485, 'Longitude': -1.351317239}, 'Gedling': {'Latitude': 53.02605385, 'Longitude': -1.107116919}, 'High Peak': {'Latitude': 53.3675462, 'Longitude': -1.852874649}, 'Mansfield': {'Latitude': 53.1443785, 'Longitude': -1.1964165}, 'Newark and Sherwood': {'Latitude': 53.10895395, 'Longitude': -0.944301798}, 'North East Derbyshire': {'Latitude': 53.2226728, 'Longitude': -1.5239286}, 'Nottingham': {'Latitude': 52.9534193, 'Longitude': -1.1496461}, 'Rushcliffe': {'Latitude': 52.91250105, 'Longitude': -1.011062229}, 'South Derbyshire': {'Latitude': 52.8224616, 'Longitude': -1.502636219}, 'Blaby': {'Latitude': 52.5731976, 'Longitude': -1.1646389}, 'Charnwood': {'Latitude': 52.7392639, 'Longitude': -1.137083278}, 'Harborough': {'Latitude': 52.53856885, 'Longitude': -0.920044489}, 'Hinckley and Bosworth': {'Latitude': 52.608409, 'Longitude': -1.417190996}, 'Leicester': {'Latitude': 52.6362, 'Longitude': -1.1331969}, 'Melton': {'Latitude': 52.8117106, 'Longitude': -0.859286729}, 'North West Leicestershire': {'Latitude': 52.7704201, 'Longitude': -1.396504669}, 'North Northamptonshire': {'Latitude': 52.41755025, 'Longitude': -0.643117541}, 'Oadby and Wigston': {'Latitude': 52.5870666, 'Longitude': -1.099780214}, 'Rutland': {'Latitude': 52.6423036, 'Longitude': -0.663264308}, 'West Northamptonshire': {'Latitude': 52.2273432, 'Longitude': -0.996746473}, 'Boston': {'Latitude': 52.9776561, 'Longitude': -0.0237985}, 'East Lindsey': {'Latitude': 53.2680103, 'Longitude': 0.012775773}, 'Lincoln': {'Latitude': 53.2293545, 'Longitude': -0.5404819}, 'North Kesteven': {'Latitude': 53.07252915, 'Longitude': -0.447353866}, 'South Holland': {'Latitude': 52.8127195, 'Longitude': -0.001262797}, 'South Kesteven': {'Latitude': 52.8502665, 'Longitude': -0.495192474}, 'West Lindsey': {'Latitude': 53.39772845, 'Longitude': -0.50352875}, 'Bedford': {'Latitude': 52.1363806, 'Longitude': -0.4675041}, 'Central Bedfordshire': {'Latitude': 51.99803275, 'Longitude': -0.479151429}, 'Dacorum': {'Latitude': 51.76895405, 'Longitude': -0.551551019}, 'East Hertfordshire': {'Latitude': 51.86567885, 'Longitude': 0.012485013}, 'Hertsmere': {'Latitude': 51.68082975, 'Longitude': -0.26811131}, 'Luton': {'Latitude': 51.89107295, 'Longitude': -0.423030408}, 'North Hertfordshire': {'Latitude': 51.95686495, 'Longitude': -0.223050908}, 'St. Albans': {'Latitude': 51.753051, 'Longitude': -0.3379675}, 'Stevenage': {'Latitude': 51.9016663, 'Longitude': -0.2027155}, 'Three Rivers': {'Latitude': 51.6701376, 'Longitude': -0.473801323}, 'Watford': {'Latitude': 51.6553875, 'Longitude': -0.3957425}, 'Welwyn Hatfield': {'Latitude': 51.77310555, 'Longitude': -0.209517053}, 'Babergh': {'Latitude': 52.06297535, 'Longitude': 0.912224157}, 'Breckland': {'Latitude': 52.5903063, 'Longitude': 0.75903631}, 'Broadland': {'Latitude': 52.6928977, 'Longitude': 1.256487519}, 'Cambridge': {'Latitude': 52.2055314, 'Longitude': 0.1186637}, 'East Cambridgeshire': {'Latitude': 52.33498865, 'Longitude': 0.262893924}, 'East Suffolk': {'Latitude': 52.24100135, 'Longitude': 1.458208931}, 'Fenland': {'Latitude': 52.56284005, 'Longitude': 0.010157722}, 'Great Yarmouth': {'Latitude': 52.6071742, 'Longitude': 1.7314845}, 'Huntingdonshire': {'Latitude': 52.37104395, 'Longitude': -0.223577893}, 'Ipswich': {'Latitude': 52.0579324, 'Longitude': 1.1528095}, "King's Lynn and West Norfolk": {'Latitude': 52.71316265, 'Longitude': 0.434874923}, 'Mid Suffolk': {'Latitude': 52.23476185, 'Longitude': 1.045134263}, 'North Norfolk': {'Latitude': 52.835652, 'Longitude': 1.127659769}, 'Norwich': {'Latitude': 52.6285576, 'Longitude': 1.2923954}, 'Peterborough': {'Latitude': 52.5725769, 'Longitude': -0.2427336}, 'South Cambridgeshire': {'Latitude': 52.17965405, 'Longitude': -0.003436813}, 'South Norfolk': {'Latitude': 52.5169106, 'Longitude': 1.366167781}, 'West Suffolk': {'Latitude': 52.25813755, 'Longitude': 0.617482578}, 'Basildon': {'Latitude': 51.5754602, 'Longitude': 0.4757363}, 'Braintree': {'Latitude': 51.8780637, 'Longitude': 0.5537161}, 'Brentwood': {'Latitude': 51.6201654, 'Longitude': 0.3018662}, 'Broxbourne': {'Latitude': 51.7465723, 'Longitude': -0.0190782}, 'Castle Point': {'Latitude': 51.54450755, 'Longitude': 0.584008407}, 'Chelmsford': {'Latitude': 51.7345329, 'Longitude': 0.4730532}, 'Colchester': {'Latitude': 51.8896903, 'Longitude': 0.8994651}, 'Epping Forest': {'Latitude': 51.6676884, 'Longitude': 0.054801129}, 'Harlow': {'Latitude': 51.7676194, 'Longitude': 0.0974893}, 'Maldon': {'Latitude': 51.731198, 'Longitude': 0.6791849}, 'Rochford': {'Latitude': 51.5840602, 'Longitude': 0.678713094}, 'Southend-on-Sea': {'Latitude': 51.5388241, 'Longitude': 0.7128137}, 'Tendring': {'Latitude': 51.8753236, 'Longitude': 1.1128842}, 'Thurrock': {'Latitude': 51.5080169, 'Longitude': 0.39628174}, 'Uttleford': {'Latitude': 51.19195, 'Longitude': -0.68283}, 'Hackney': {'Latitude': 51.5432402, 'Longitude': -0.0493621}, 'Lewisham': {'Latitude': 51.4624292, 'Longitude': -0.0101787}, 'Southwark': {'Latitude': 51.46525455, 'Longitude': -0.069018633}, 'Tower Hamlets': {'Latitude': 51.1288633, 'Longitude': 1.2986686}, 'Camden': {'Latitude': 51.54279655, 'Longitude': -0.162480314}, 'City of London': {'Latitude': 51.5156177, 'Longitude': -0.0919983}, 'Hammersmith and Fulham': {'Latitude': 51.4983142, 'Longitude': -0.227878184}, 'Islington': {'Latitude': 51.5384287, 'Longitude': -0.0999051}, 'Kensington and Chelsea': {'Latitude': 51.50379515, 'Longitude': -0.200789383}, 'Lambeth': {'Latitude': 51.4952111, 'Longitude': -0.1163354}, 'Wandsworth': {'Latitude': 51.4570271, 'Longitude': -0.1932607}, 'Westminster': {'Latitude': 51.5004439, 'Longitude': -0.1265398}, 'Barking and Dagenham': {'Latitude': 51.5540907, 'Longitude': 0.150488888}, 'Bexley': {'Latitude': 51.4416793, 'Longitude': 0.150488}, 'Enfield': {'Latitude': 51.6520851, 'Longitude': -0.0810175}, 'Greenwich': {'Latitude': 51.46862565, 'Longitude': 0.048830573}, 'Haringey': {'Latitude': 51.58792985, 'Longitude': -0.105417713}, 'Havering': {'Latitude': 51.54437325, 'Longitude': -0.1443138}, 'Newham': {'Latitude': 51.5300157, 'Longitude': 0.029309079}, 'Redbridge': {'Latitude': 51.5763203, 'Longitude': 0.0454097}, 'Waltham Forest': {'Latitude': 51.59816935, 'Longitude': -0.017836675}, 'Bromley': {'Latitude': 51.36685695, 'Longitude': 0.061709076}, 'Croydon': {'Latitude': 51.3713049, 'Longitude': -0.101957}, 'Kingston Upon Thames': {'Latitude': 51.4096275, 'Longitude': -0.3062621}, 'Merton': {'Latitude': 51.41086985, 'Longitude': -0.188097089}, 'Richmond Upon Thames': {'Latitude': 51.4405529, 'Longitude': -0.307639438}, 'Sutton': {'Latitude': 51.35746445, 'Longitude': -0.173626895}, 'Barnet': {'Latitude': 51.65309, 'Longitude': -0.2002261}, 'Brent': {'Latitude': 52.608077, 'Longitude': -1.6745079}, 'Ealing': {'Latitude': 51.5126553, 'Longitude': -0.3051952}, 'Harrow': {'Latitude': 51.59682715, 'Longitude': -0.337304618}, 'Hillingdon': {'Latitude': 51.5425193, 'Longitude': -0.448334931}, 'Hounslow': {'Latitude': 51.4686132, 'Longitude': -0.3613471}, 'Gateshead': {'Latitude': 54.9625789, 'Longitude': -1.6019294}, 'Newcastle upon Tyne': {'Latitude': 54.9738474, 'Longitude': -1.6131572}, 'North Tyneside': {'Latitude': 55.02979945, 'Longitude': -1.508256}, 'Northumberland': {'Latitude': 55.25, 'Longitude': -2.000559}, 'South Tyneside': {'Latitude': 54.96987425, 'Longitude': -1.447680547}, 'Sunderland': {'Latitude': 54.9058512, 'Longitude': -1.3828727}, 'County Durham': {'Latitude': 54.68483225, 'Longitude': -1.77401717}, 'Darlington': {'Latitude': 54.5242081, 'Longitude': -1.5555812}, 'Hartlepool': {'Latitude': 54.6857276, 'Longitude': -1.2093696}, 'Middlesbrough': {'Latitude': 54.5760419, 'Longitude': -1.2344047}, 'Redcar and Cleveland': {'Latitude': 54.5679056, 'Longitude': -1.005496317}, 'Stockton-on-Tees': {'Latitude': 54.564094, 'Longitude': -1.3129164}, 'Cheshire East': {'Latitude': 53.1673422, 'Longitude': -2.292880278}, 'Cheshire West and Chester': {'Latitude': 53.16379785, 'Longitude': -2.728536114}, 'Halton': {'Latitude': 53.35385255, 'Longitude': -2.742782879}, 'Warrington': {'Latitude': 53.4018582, 'Longitude': -2.56802236}, 'Allerdale': {'Latitude': 54.70888095, 'Longitude': -3.252788011}, 'Barrow-in-Furness': {'Latitude': 54.1288796, 'Longitude': -3.226900821}, 'Carlisle': {'Latitude': 54.8948478, 'Longitude': -2.9362311}, 'Copeland': {'Latitude': 54.3876165, 'Longitude': -3.33112534}, 'Eden': {'Latitude': 54.6056481, 'Longitude': -2.671522203}, 'South Lakeland': {'Latitude': 54.2720691, 'Longitude': -2.771361687}, 'Bolton': {'Latitude': 53.5782863, 'Longitude': -2.4300367}, 'Bury': {'Latitude': 53.5927543, 'Longitude': -2.2972827}, 'Manchester': {'Latitude': 53.4794892, 'Longitude': -2.2451148}, 'Oldham': {'Latitude': 53.5415797, 'Longitude': -2.1147831}, 'Rochdale': {'Latitude': 53.6153659, 'Longitude': -2.1557561}, 'Salford': {'Latitude': 53.4877463, 'Longitude': -2.2891921}, 'Stockport': {'Latitude': 53.407901, 'Longitude': -2.160243}, 'Tameside': {'Latitude': 53.4786454, 'Longitude': -2.077021163},
            'Trafford': {'Latitude': 53.41893605, 'Longitude': -2.359297161}, 'Wigan': {'Latitude': 53.5457188, 'Longitude': -2.6264624}, 'Blackburn with Darwen': {'Latitude': 53.69917695, 'Longitude': -2.470900095}, 'Blackpool': {'Latitude': 53.8179442, 'Longitude': -3.0509812}, 'Burnley': {'Latitude': 53.7907262, 'Longitude': -2.2439196}, 'Chorley': {'Latitude': 53.6531915, 'Longitude': -2.6294313}, 'Fylde': {'Latitude': 53.79336215, 'Longitude': -2.89426008}, 'Hyndburn': {'Latitude': 53.7607317, 'Longitude': -2.390054914}, 'Lancaster': {'Latitude': 54.0484068, 'Longitude': -2.7990345}, 'Pendle': {'Latitude': 53.87904015, 'Longitude': -2.17177953}, 'Preston': {'Latitude': 53.7593363, 'Longitude': -2.6992717}, 'Ribble Valley': {'Latitude': 53.90264405, 'Longitude': -2.422856035}, 'Rossendale': {'Latitude': 53.6848806, 'Longitude': -2.261439759}, 'South Ribble': {'Latitude': 53.72715265, 'Longitude': -2.733006646}, 'West Lancashire': {'Latitude': 53.6109397, 'Longitude': -2.856571333}, 'Wyre': {'Latitude': 53.9000859, 'Longitude': -2.838953226}, 'Knowsley': {'Latitude': 53.4552358, 'Longitude': -2.8546852}, 'Liverpool': {'Latitude': 53.4071991, 'Longitude': -2.99168}, 'Sefton': {'Latitude': 53.5034122, 'Longitude': -2.9714708}, 'St. Helens': {'Latitude': 53.4486075, 'Longitude': -2.735982079}, 'Wirral': {'Latitude': 53.3409714, 'Longitude': -3.0500916}, 'Bracknell Forest': {'Latitude': 51.4002688, 'Longitude': -0.741788801}, 'Buckinghamshire': {'Latitude': 51.840894, 'Longitude': -0.899807359}, 'Cherwell': {'Latitude': 51.9747169, 'Longitude': -1.226294104}, 'Milton Keynes': {'Latitude': 52.0406502, 'Longitude': -0.7594092}, 'Oxford': {'Latitude': 51.7520131, 'Longitude': -1.2578499}, 'Reading': {'Latitude': 51.4564242, 'Longitude': -0.9700664}, 'Slough': {'Latitude': 51.5111014, 'Longitude': -0.5940682}, 'South Oxfordshire': {'Latitude': 51.6366088, 'Longitude': -1.080497185}, 'Vale of White Horse': {'Latitude': 51.654201, 'Longitude': -1.485703471}, 'West Berkshire': {'Latitude': 51.44631345, 'Longitude': -1.275881955}, 'West Oxfordshire': {'Latitude': 51.84036295, 'Longitude': -1.512127444}, 'Windsor and Maidenhead': {'Latitude': 51.4803412, 'Longitude': -0.67695052}, 'Wokingham': {'Latitude': 51.4570846, 'Longitude': -0.88653703}, 'Basingstoke and Deane': {'Latitude': 51.2587797, 'Longitude': -1.221107318}, 'East Hampshire': {'Latitude': 51.07788895, 'Longitude': -0.943907586}, 'Eastleigh': {'Latitude': 50.9202337, 'Longitude': -1.29926562}, 'Fareham': {'Latitude': 50.8526637, 'Longitude': -1.1783134}, 'Gosport': {'Latitude': 50.7952074, 'Longitude': -1.1210853}, 'Hart': {'Latitude': 51.2761671, 'Longitude': -0.892798981}, 'Havant': {'Latitude': 50.8334197, 'Longitude': -0.982658943}, 'Isle of Wight': {'Latitude': 50.67108245, 'Longitude': -1.33280428}, 'New Forest': {'Latitude': 50.8556349, 'Longitude': -1.595562813}, 'Portsmouth': {'Latitude': 50.800031, 'Longitude': -1.0906023}, 'Rushmoor': {'Latitude': 51.27523885, 'Longitude': -0.769391729}, 'Southampton': {'Latitude': 50.9025349, 'Longitude': -1.404189}, 'Test Valley': {'Latitude': 51.13379045, 'Longitude': -1.518286427}, 'Winchester': {'Latitude': 51.0612766, 'Longitude': -1.3131692}, 'Ashford': {'Latitude': 51.148555, 'Longitude': 0.8722566}, 'Canterbury': {'Latitude': 51.2800275, 'Longitude': 1.0802533}, 'Dartford': {'Latitude': 51.4443059, 'Longitude': 0.21807}, 'Dover': {'Latitude': 51.1251275, 'Longitude': 1.3134228}, 'Folkestone & Hythe': {'Latitude': 51.05774845, 'Longitude': 1.00607207}, 'Gravesham': {'Latitude': 51.39723695, 'Longitude': 0.396172587}, 'Maidstone': {'Latitude': 51.2748258, 'Longitude': 0.5231646}, 'Medway': {'Latitude': 51.4157386, 'Longitude': 0.568730851}, 'Sevenoaks': {'Latitude': 51.27452185, 'Longitude': 0.196116556}, 'Swale': {'Latitude': 51.3367451, 'Longitude': 0.801369799}, 'Thanet': {'Latitude': 51.35330455, 'Longitude': 1.331986597}, 'Tonbridge and Malling': {'Latitude': 51.2717306, 'Longitude': 0.356659801}, 'Tunbridge Wells': {'Latitude': 51.1371483, 'Longitude': 0.2673446}, 'Adur': {'Latitude': 50.8453169, 'Longitude': -0.293988661}, 'Arun': {'Latitude': 50.8312375, 'Longitude': -0.566705867}, 'Brighton and Hove': {'Latitude': 50.8453169, 'Longitude': -0.149746898}, 'Chichester': {'Latitude': 50.84467705, 'Longitude': -0.783114432}, 'Crawley': {'Latitude': 51.1103444, 'Longitude': -0.1801094}, 'Eastbourne': {'Latitude': 50.7664372, 'Longitude': 0.2781546}, 'Elmbridge': {'Latitude': 52.308409, 'Longitude': -2.1474369}, 'Epsom and Ewell': {'Latitude': 51.3363098, 'Longitude': -0.267381693}, 'Guildford': {'Latitude': 51.2356068, 'Longitude': -0.5732063}, 'Hastings': {'Latitude': 50.8553888, 'Longitude': 0.5824703}, 'Horsham': {'Latitude': 51.0630273, 'Longitude': -0.3295028}, 'Lewes': {'Latitude': 50.8746139, 'Longitude': 0.005115324}, 'Mid Sussex': {'Latitude': 51.0053398, 'Longitude': -0.127311344}, 'Mole Valley': {'Latitude': 51.22009445, 'Longitude': -0.334755193}, 'Reigate and Banstead': {'Latitude': 51.25164045, 'Longitude': -0.186468215}, 'Rother': {'Latitude': 50.9514264, 'Longitude': 0.57404899}, 'Runnymede': {'Latitude': 51.3948374, 'Longitude': -0.551960946}, 'Spelthorne': {'Latitude': 51.4250347, 'Longitude': -0.459286076}, 'Surrey Heath': {'Latitude': 51.33588905, 'Longitude': -0.691653419}, 'Tandridge': {'Latitude': 51.2393372, 'Longitude': -0.0344318}, 'Waverley': {'Latitude': 51.158323, 'Longitude': -0.623321607}, 'Wealden': {'Latitude': 50.94216925, 'Longitude': 0.197280129}, 'Woking': {'Latitude': 51.3201891, 'Longitude': -0.5564726}, 'Worthing': {'Latitude': 50.8115402, 'Longitude': -0.3699697}, 'Cornwall': {'Latitude': 50.4433489, 'Longitude': -4.624656585}, 'Isles of Scilly': {'Latitude': 49.92034085, 'Longitude': -6.292879121}, 'East Devon': {'Latitude': 50.7568771, 'Longitude': -3.221564289}, 'Exeter': {'Latitude': 50.7255794, 'Longitude': -3.5269497}, 'Mid Devon': {'Latitude': 50.86839225, 'Longitude': -3.59969999}, 'North Devon': {'Latitude': 51.061456, 'Longitude': -3.923923298}, 'Plymouth': {'Latitude': 50.3714122, 'Longitude': -4.1424451}, 'South Hams': {'Latitude': 50.3720497, 'Longitude': -3.816251991}, 'Teignbridge': {'Latitude': 50.6125552, 'Longitude': -3.655910598}, 'Torbay': {'Latitude': 50.446247, 'Longitude': -3.539499814}, 'Torridge': {'Latitude': 50.86260145, 'Longitude': -4.261205563}, 'West Devon': {'Latitude': 50.65199745, 'Longitude': -4.074310854}, 'Bournemouth, Christchurch and Poole': {'Latitude': 50.766281, 'Longitude': -1.7976771}, 'Dorset': {'Latitude': 50.79683685, 'Longitude': -2.344732261}, 'Mendip': {'Latitude': 51.1943905, 'Longitude': -2.54192211}, 'Sedgemoor': {'Latitude': 51.1868339, 'Longitude': -2.968421232}, 'Somerset West and Taunton': {'Latitude': 51.06267465, 'Longitude': -3.346932006}, 'South Somerset': {'Latitude': 50.9843053, 'Longitude': -2.77615618}, 'Bath and North East Somerset': {'Latitude': 51.35632375, 'Longitude': -2.486661425}, 'Bristol': {'Latitude': 51.4538022, 'Longitude': -2.5972985}, 'Cheltenham': {'Latitude': 51.8995685, 'Longitude': -2.0711559}, 'Cotswold': {'Latitude': 51.84516805, 'Longitude': -1.8913308}, 'Forest of Dean': {'Latitude': 51.7996179, 'Longitude': -2.530584163}, 'Gloucester': {'Latitude': 51.8653705, 'Longitude': -2.2458192}, 'North Somerset': {'Latitude': 51.39663045, 'Longitude': -2.769128924}, 'South Gloucestershire': {'Latitude': 51.54919165, 'Longitude': -2.480952817}, 'Stroud': {'Latitude': 51.745424, 'Longitude': -2.2198605}, 'Swindon': {'Latitude': 51.5613683, 'Longitude': -1.7856853}, 'Tewkesbury': {'Latitude': 51.9925394, 'Longitude': -2.156016959}, 'Wiltshire': {'Latitude': 51.324162, 'Longitude': -1.90324867}, 'Bromsgrove': {'Latitude': 52.3390519, 'Longitude': -2.053201799}, 'Herefordshire': {'Latitude': 52.083333, 'Longitude': -2.75}, 'Malvern Hills': {'Latitude': 52.1675333, 'Longitude': -2.331160204}, 'North Warwickshire': {'Latitude': 52.561361, 'Longitude': -1.629634444}, 'Nuneaton and Bedworth': {'Latitude': 52.5010313, 'Longitude': -1.467739194}, 'Redditch': {'Latitude': 52.3057655, 'Longitude': -1.9417444}, 'Rugby': {'Latitude': 52.3726682, 'Longitude': -1.2620038}, 'Stratford-on-Avon': {'Latitude': 52.1927803, 'Longitude': -1.70634}, 'Warwick': {'Latitude': 52.2814519, 'Longitude': -1.5815742}, 'Worcester': {'Latitude': 52.1911849, 'Longitude': -2.2206585}, 'Wychavon': {'Latitude': 52.1803417, 'Longitude': -2.062313673}, 'Wyre Forest': {'Latitude': 52.38505915, 'Longitude': -2.234796614}, 'Cannock Chase': {'Latitude': 52.7069197, 'Longitude': -1.978434755}, 'East Staffordshire': {'Latitude': 52.8878642, 'Longitude': -1.903080245}, 'Lichfield': {'Latitude': 52.68064, 'Longitude': -1.824399172}, 'Newcastle-under-Lyme': {'Latitude': 53.0117627, 'Longitude': -2.2273919}, 'Shropshire': {'Latitude': 52.65233935, 'Longitude': -2.64356407}, 'South Staffordshire': {'Latitude': 52.6047717, 'Longitude': -2.259164839}, 'Stafford': {'Latitude': 52.8063157, 'Longitude': -2.1163818}, 'Staffordshire Moorlands': {'Latitude': 53.07155675, 'Longitude': -1.974200712}, 'Stoke-on-Trent': {'Latitude': 53.0162014, 'Longitude': -2.1812607}, 'Tamworth': {'Latitude': 52.6345819, 'Longitude': -1.6948438}, 'Telford and Wrekin': {'Latitude': 52.72144515, 'Longitude': -2.500862392}, 'Birmingham': {'Latitude': 52.4796992, 'Longitude': -1.9026911}, 'Coventry': {'Latitude': 52.4081812, 'Longitude': -1.510477}, 'Dudley': {'Latitude': 52.5110832, 'Longitude': -2.0816813}, 'Sandwell': {'Latitude': 52.5151278, 'Longitude': -2.013562374}, 'Solihull': {'Latitude': 52.4130189, 'Longitude': -1.7768935}, 'Walsall': {'Latitude': 52.5847949, 'Longitude': -1.9822687}, 'Wolverhampton': {'Latitude': 52.5847651, 'Longitude': -2.127567}, 'East Riding of Yorkshire': {'Latitude': 53.9112323, 'Longitude': -0.5813105}, 'Kingston upon Hull, City of': {'Latitude': 53.76238625, 'Longitude': -0.330121376}, 'North East Lincolnshire': {'Latitude': 53.53680335, 'Longitude': -0.093681013}, 'North Lincolnshire': {'Latitude': 53.5897441, 'Longitude': -0.60232303}, 'Craven': {'Latitude': 54.05375295, 'Longitude': -2.161512381}, 'Hambleton': {'Latitude': 54.25045835, 'Longitude': -1.436878304}, 'Harrogate': {'Latitude': 53.9921491, 'Longitude': -1.5391039}, 'Richmondshire': {'Latitude': 54.3574047, 'Longitude': -1.984952497}, 'Ryedale': {'Latitude': 54.1984242, 'Longitude': -0.861424611}, 'Scarborough': {'Latitude': 54.2820009, 'Longitude': -0.4011868}, 'Selby': {'Latitude': 53.785097, 'Longitude': -1.09904072}, 'York': {'Latitude': 53.9590555, 'Longitude': -1.0815361}, 'Barnsley': {'Latitude': 53.5527719, 'Longitude': -1.4827755}, 'Doncaster': {'Latitude': 53.5227681, 'Longitude': -1.1335312}, 'Rotherham': {'Latitude': 53.4310417, 'Longitude': -1.355187}, 'Sheffield': {'Latitude': 53.3806626, 'Longitude': -1.4702278}, 'Bradford': {'Latitude': 53.7944229, 'Longitude': -1.7519186}, 'Calderdale': {'Latitude': 53.7204748, 'Longitude': -1.962288633}, 'Kirklees': {'Latitude': 53.64226345, 'Longitude': -1.780943269}, 'Leeds': {'Latitude': 53.7974185, 'Longitude': -1.5437941}, 'Wakefield': {'Latitude': 53.6829541, 'Longitude': -1.4967286}, 'Derbyshire and Nottinghamshire': {'Latitude': 53.01965335, 'Longitude': -1.335508459}, 'Leicestershire, Rutland and Northamptonshire': {'Latitude': 52.65355, 'Longitude': -0.76758}, 'Lincolnshire': {'Latitude': 53.1823034, 'Longitude': -0.203120854}, 'Bedfordshire and Hertfordshire': {'Latitude': 52.08354285, 'Longitude': -0.39130704}, 'East Anglia': {'Latitude': 51.4510191, 'Longitude': -0.99349144}, 'Essex': {'Latitude': 51.77046785, 'Longitude': 0.464669774}, 'Inner London - East': {'Latitude': 51.5084252, 'Longitude': -0.076122891}, 'Inner London - West': {'Latitude': 51.51374175, 'Longitude': -0.110931954}, 'Outer London - East and North East': {'Latitude': 51.404449, 'Longitude': -2.31482}, 'Outer London - South': {'Latitude': 51.5131805, 'Longitude': -0.1122093}, 'Outer London - West and North West': {'Latitude': 51.53356, 'Longitude': -0.10787}, 'Northumberland, and Tyne and Wear': {'Latitude': 54.9116178, 'Longitude': -1.5129857}, 'Tees Valley and Durham': {'Latitude': 54.5937984, 'Longitude': -1.3564458}, 'Cheshire': {'Latitude': 53.2141028, 'Longitude': -2.471770086}, 'Cumbria': {'Latitude': 54.6143136, 'Longitude': -2.942089947}, 'Greater Manchester': {'Latitude': 53.50652485, 'Longitude': -2.337440142}, 'Lancashire': {'Latitude': 53.8611703, 'Longitude': -2.565088792}, 'Merseyside': {'Latitude': 53.4953602, 'Longitude': -2.97393796}, 'Berkshire, Buckinghamshire and Oxfordshire': {'Latitude': 51.83333, 'Longitude': -1.25}, 'Hampshire and Isle of Wight': {'Latitude': 51.04483545, 'Longitude': -1.24340936}, 'Kent': {'Latitude': 51.20707485, 'Longitude': 0.721036181}, 'Surrey, East and West Sussex': {'Latitude': 51.0, 'Longitude': -0.41667}, 'Cornwall and Isles of Scilly': {'Latitude': 50.416667, 'Longitude': -4.75}, 'Devon': {'Latitude': 50.7241405, 'Longitude': -3.660778816}, 'Dorset and Somerset': {'Latitude': 51.3696769, 'Longitude': -2.366195}, 'Gloucestershire, Wiltshire and Bath/Bristol area': {'Latitude': 51.45523, 'Longitude': -2.59665}, 'Herefordshire, Worcestershire and Warwickshire': {'Latitude': 52.33333, 'Longitude': -1.58333}, 'Shropshire and Staffordshire': {'Latitude': 53.0131742, 'Longitude': -2.5247441}, 'West Midlands': {'Latitude': 52.5050033, 'Longitude': -1.964396123}, 'East Yorkshire and Northern Lincolnshire': {'Latitude': 53.16667, 'Longitude': -0.25}, 'North Yorkshire': {'Latitude': 54.13453275, 'Longitude': -1.498628491}, 'South Yorkshire': {'Latitude': 53.48153335, 'Longitude': -1.381042207}, 'West Yorkshire': {'Latitude': 53.7414271, 'Longitude': -1.720200377}, 'East Midlands': {'Latitude': 52.7965611, 'Longitude': -0.671794756}, 'East of England': {'Latitude': 52.2199774, 'Longitude': 0.487577747}, 'London': {'Latitude': 51.4893335, 'Longitude': -0.144055085}, 'North East': {'Latitude': 54.73141115, 'Longitude': -1.791981336}, 'North West': {'Latitude': 52.9559076, 'Longitude': -1.1557387}, 'South East': {'Latitude': 51.4680988, 'Longitude': -0.0666715}, 'South West': {'Latitude': 51.4757777, 'Longitude': -0.398576131}, 'Yorkshire and The Humber': {'Latitude': 53.9318994, 'Longitude': -1.166471661}, 'England': {'Latitude': 52.56453, 'Longitude': -1.467108403}
}
#DATA PREP SECTION--------------------------------------------



    #remove common unwanted columns from all of the files
columns_to_remove = ['measure', 'gss_code', 'geography']

df_ctry.drop(columns=columns_to_remove, inplace=True)
df_rgn.drop(columns=columns_to_remove, inplace=True)
df_itl.drop(columns=columns_to_remove, inplace=True)
df_lad.drop(columns=columns_to_remove, inplace=True)

#datetime format
df_ctry['extract_date'] = pd.to_datetime(df_ctry['extract_date'], format='%Y-%m-%d')
df_rgn['extract_date'] = pd.to_datetime(df_rgn['extract_date'], format='%Y-%m-%d')
df_itl['extract_date'] = pd.to_datetime(df_itl['extract_date'], format='%Y-%m-%d')
df_lad['extract_date'] = pd.to_datetime(df_lad['extract_date'], format='%Y-%m-%d')


#FEATURE ENGINEERING for ctry

df_ctry['Latitude'] = df_ctry['gss_name'].map(lambda x: longlat[x]['Latitude'] if x in longlat else '')
df_ctry['Longitude'] = df_ctry['gss_name'].map(lambda x: longlat[x]['Longitude'] if x in longlat else '')
    #FEATURE ENGINEERING for rgn
        #create new column called Country and fill all rows with the value England
df_rgn["Country"] = "England"
df_rgn['Latitude'] = df_rgn['gss_name'].map(lambda x: longlat[x]['Latitude'] if x in longlat else '')
df_rgn['Longitude'] = df_rgn['gss_name'].map(lambda x: longlat[x]['Longitude'] if x in longlat else '')


    #FEATURE ENGINEERING for itl
        #create new columns called Country and Region. Fill Country with England and use dictionary to fill Region rows 
        #then move the Region column next to gss_name column
df_itl["Country"] = "England"
df_itl['Region'] = df_itl['gss_name'].map(region_mapping)
df_itl['Latitude'] = df_itl['gss_name'].map(lambda x: longlat[x]['Latitude'] if x in longlat else '')
df_itl['Longitude'] = df_itl['gss_name'].map(lambda x: longlat[x]['Longitude'] if x in longlat else '')


    #FEATURE ENGINEERING for lad
        #create new column called Country, Region and ITL 2 and use dictionary to fill rows 
        #then move Country, Region and ITL 2 column next to gss_name column
df_lad['Country'] = df_lad['gss_name'].map(lambda x: location_data[x]['Country'] if x in location_data else '')
df_lad['Region'] = df_lad['gss_name'].map(lambda x: location_data[x]['Region'] if x in location_data else '')
df_lad['ITL 2'] = df_lad['gss_name'].map(lambda x: location_data[x]['ITL 2'] if x in location_data else '')
df_lad['Latitude'] = df_lad['gss_name'].map(lambda x: longlat[x]['Latitude'] if x in longlat else '')
df_lad['Longitude'] = df_lad['gss_name'].map(lambda x: longlat[x]['Longitude'] if x in longlat else '')

#organise
df_ctry = df_ctry[['gss_name', 'Latitude', 'Longitude'] + [col for col in df_ctry.columns if col not in ['gss_name', 'Latitude', 'Longitude']]]
df_rgn = df_rgn[['Country', 'gss_name', 'Latitude', 'Longitude'] + [col for col in df_rgn.columns if col not in ['Country', 'gss_name', 'Latitude', 'Longitude']]]
df_itl = df_itl[['Country', 'Region', 'gss_name', 'Latitude', 'Longitude'] + [col for col in df_itl.columns if col not in ['Country', 'Region', 'gss_name', 'Latitude', 'Longitude']]]
df_lad = df_lad[['Country', 'Region', 'ITL 2', 'gss_name', 'Latitude', 'Longitude'] + [col for col in df_lad.columns if col not in ['Country', 'Region', 'ITL 2', 'gss_name', 'Latitude', 'Longitude']]]



#Rename gss_name to appropriate name for each file
df_ctry.rename(columns={'gss_name': 'Country'}, inplace=True)
df_rgn.rename(columns={'gss_name': 'Region'}, inplace=True)
df_itl.rename(columns={'gss_name': 'ITL 2'}, inplace=True)
df_lad.rename(columns={'gss_name': 'LAD'}, inplace=True)

#create output files
output_ctry = current_directory.parent.parent / "assigneddata" / "prepared_ctry.csv"
output_rgn = current_directory.parent.parent / "assigneddata" / "prepared_rgn.csv"
output_itl = current_directory.parent.parent / "assigneddata" / "prepared_itl.csv"
output_lad = current_directory.parent.parent / "assigneddata" / "prepared_lad.csv"

df_ctry.to_csv(output_ctry, index=False)
df_rgn.to_csv(output_rgn, index=False)
df_itl.to_csv(output_itl, index=False)
df_lad.to_csv(output_lad, index=False)
print("Geocoding and CSV update complete.")
