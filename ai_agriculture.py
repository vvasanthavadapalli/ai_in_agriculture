# ============================================================
# Python Fundamentals Lab
# Project 4: AI in Agriculture
# ============================================================

# ------------------------------------------------------------
# 1. CROP DATA
# Store crop data as a list of tuples:
# (crop, season1, season2)
# Yield is measured in tonnes per hectare.
# ------------------------------------------------------------

crops = [
    ("Rice", 4.2, 4.8),
    ("Wheat", 3.5, 3.9),
    ("Maize", 5.0, 5.6),
    ("Cotton", 2.8, 3.1),
    ("Groundnut", 2.4, 2.7)
]


# ------------------------------------------------------------
# 2. FUNCTION
# Calculate percentage change for each crop.
# ------------------------------------------------------------

def percentage_change(season1, season2):
    return ((season2 - season1) / season1) * 100


# ------------------------------------------------------------
# 3. CALCULATE PERCENTAGE CHANGE
# Use a loop to process every crop.
# ------------------------------------------------------------

results = []

for crop, season1, season2 in crops:

    change = percentage_change(season1, season2)

    # Conditional to check whether the yield increased
    if change >= 0:
        status = "Increased"
    else:
        status = "Decreased"

    results.append((crop, season1, season2, change, status))


# ------------------------------------------------------------
# 4. FIND BEST AND WORST PERFORMING CROPS
# Use max() and min() as required.
# ------------------------------------------------------------

best_crop = max(results, key=lambda x: x[3])
worst_crop = min(results, key=lambda x: x[3])


# ------------------------------------------------------------
# 5. FUNCTION TO CREATE ONE TABLE ROW
# ------------------------------------------------------------

def make_row(result):

    crop, season1, season2, change, status = result

    # Highlight the best performing crop
    if crop == best_crop[0]:
        return f"""
        <tr class="best">
            <td><strong>{crop}</strong></td>
            <td>{season1:.1f}</td>
            <td>{season2:.1f}</td>
            <td>{change:.2f}%</td>
            <td>{status}</td>
        </tr>
        """
    else:
        return f"""
        <tr>
            <td>{crop}</td>
            <td>{season1:.1f}</td>
            <td>{season2:.1f}</td>
            <td>{change:.2f}%</td>
            <td>{status}</td>
        </tr>
        """


# ------------------------------------------------------------
# 6. GENERATE TABLE ROWS USING A PYTHON LOOP
# ------------------------------------------------------------

rows = ""

for result in results:
    rows += make_row(result)


# ------------------------------------------------------------
# 7. CREATE THE HTML PAGE
# CSS is included inside the Python f-string.
# ------------------------------------------------------------

title = "AI in Agriculture"

html = f"""
<!DOCTYPE html>
<html>

<head>

    <title>{title}</title>

    <style>

        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f8f3;
            color: #333;
        }}

        h1 {{
            text-align: center;
            color: #2d6a4f;
        }}

        h2 {{
            color: #40916c;
            margin-top: 30px;
        }}

        .intro {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 25px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background-color: white;
        }}

        th {{
            background-color: #40916c;
            color: white;
            padding: 12px;
        }}

        td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: center;
        }}

        .best {{
            background-color: #d8f3dc;
        }}

        .result {{
            background-color: white;
            padding: 20px;
            margin-top: 25px;
            border-radius: 10px;
        }}

        .ai-section {{
            background-color: white;
            padding: 20px;
            margin-top: 25px;
            border-radius: 10px;
        }}

        li {{
            margin: 10px;
        }}

    </style>

</head>


<body>

    <!-- Main title -->

    <h1>{title}</h1>


    <!-- Short introduction -->

    <div class="intro">

        <h2>Introduction</h2>

        <p>
            Artificial Intelligence is becoming useful in modern
            agriculture. It can help farmers detect crop diseases,
            predict crop yields and monitor fields using agricultural
            drones. AI can analyse agricultural data and help farmers
            make better decisions.
        </p>

    </div>


    <!-- Crop yield comparison -->

    <h2>Crop Yield Comparison</h2>

    <table>

        <tr>
            <th>Crop</th>
            <th>Season 1 Yield<br>(tonnes/hectare)</th>
            <th>Season 2 Yield<br>(tonnes/hectare)</th>
            <th>Percentage Change</th>
            <th>Status</th>
        </tr>

        {rows}

    </table>


    <!-- Best and worst performing crops -->

    <div class="result">

        <h2>Performance Results</h2>

        <p>
            <strong>Best Performing Crop:</strong>
            {best_crop[0]}
            ({best_crop[3]:.2f}% increase)
        </p>

        <p>
            <strong>Worst Performing Crop:</strong>
            {worst_crop[0]}
            ({worst_crop[3]:.2f}% increase)
        </p>

    </div>


    <!-- How AI helps -->

    <div class="ai-section">

        <h2>How AI Helps</h2>

        <ul>

            <li>
                AI can help farmers detect crop diseases
                by analysing pictures of plants.
            </li>

            <li>
                AI can use agricultural data to help predict
                how much crop a farmer may produce.
            </li>

            <li>
                AI-powered drones can monitor crops and
                help farmers observe their fields.
            </li>

        </ul>

    </div>


</body>

</html>
"""


# ------------------------------------------------------------
# 8. SAVE THE WEBPAGE
# Use Python file handling to create index.html.
# ------------------------------------------------------------

with open("index.html", "w") as file:
    file.write(html)


print("Webpage created successfully: index.html")