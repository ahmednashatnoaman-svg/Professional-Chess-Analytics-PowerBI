# 🏆 Master Guide: Professional Chess Power BI Dashboard

This guide is your exact checklist. Follow these steps linearly from opening Power BI to your final GitHub push. Because AI cannot directly edit `.pbix` binary files, you will act as the architect inside the Power BI app using the code and assets I have generated for you.

---

## Step 1: Open and Setup
1. **Open Power BI Desktop** on your computer.
2. Go to **File > Open report** and select `Chess-Power-BI-Dashboard-Repo/dashboard/Chess Dashboard.pbix`.
3. If there is old data in the file, go to the right-hand **Data** pane, right-click the old `games` table, and select **Delete from model**. We are replacing it with our advanced Star Schema.

## Step 2: Import the Professional Data
1. In the top ribbon, click **Get Data > Text/CSV**.
2. Navigate to your `data/` folder. 
3. Select `Fact_Games.csv` and click **Load**. (Do *not* click Combine).
4. Repeat this exact process for the other three dimension tables: 
   * `Dim_Openings.csv`
   * `Dim_Players.csv`
   * `Dim_TimeControls.csv`

## Step 3: Build the Star Schema (The Brains)
1. Go to the **Model View** (the icon with 3 interconnected boxes on the far left of Power BI).
2. You will see your 4 tables. Arrange `Fact_Games` in the center.
3. Drag and drop to connect the keys:
   * Drag `Opening_ID` from `Dim_Openings` and drop it onto `Opening_ID` in `Fact_Games`.
   * Drag `TimeControl_ID` from `Dim_TimeControls` and drop it onto `TimeControl_ID` in `Fact_Games`.
   * **The Player Challenge (Role-Playing Dimension):** `Fact_Games` has both `white_id` and `black_id`. You cannot connect both actively to `Dim_Players`. 
   * **The Pro Solution:** Go to the "Data" pane, right click `Dim_Players`, and copy/paste it to create two tables. Rename one to `Dim_White_Player` and connect its `Player_ID` to `white_id`. Rename the other to `Dim_Black_Player` and connect its `Player_ID` to `black_id`.

## Step 4: Apply the Premium UI Design (The Looks)
1. Switch back to the **Report View** (the chart icon on the far left).
2. **Apply the Theme:**
   * Go to the **View** ribbon at the top.
   * Click the dropdown arrow in the **Themes** gallery.
   * Select **Browse for themes**.
   * Choose `assets/professional_chess_theme.json`. (This automatically styles your fonts, charts, and colors).
3. **Apply the Background:**
   * Click anywhere on the blank white canvas.
   * Open the **Format page** panel on the right (the paint roller/brush icon).
   * Expand **Canvas Background**.
   * Click **Browse...** and select `assets/dashboard_bg.png`.
   * **CRITICAL:** Set **Transparency to 0%** and **Image Fit to 'Fit'**.

## Step 5: Add the Advanced DAX Measures (The Expertise)
1. In the **Data** pane on the right, right-click the `Fact_Games` table and select **New Measure**.
2. Open the `dashboard/DAX_Measures.md` file in your code editor.
3. Copy the formula for `Total Games` and paste it into the Power BI formula bar, then hit Enter.
4. Repeat this process for all the measures in the DAX file (e.g., `Win % (White)`, `Total Upsets`, `Avg Turns`).

## Step 6: Build Your Visuals
1. **KPI Cards:** Add "Card" visuals to the top of your background. Drag your new `Total Games`, `Total Upsets`, and `Win %` measures into them.
2. **Bar Charts:** Add a Clustered Bar Chart. Put `Dim_Openings[Opening_Family]` on the Y-axis and `Total Games` on the X-axis to see the most popular openings.
3. **Line Charts:** Add a Line chart. Put `Dim_Players[Player_Tier]` on the X-axis and `Win %` on the Y-axis to see how win rates change as players get more advanced.
4. *Because of the JSON theme, your charts will automatically have transparent backgrounds and fit perfectly onto the glassmorphism background!*

## Step 7: Save, Close, and Push to GitHub
1. Once your dashboard looks perfect, go to **File > Save**.
2. Close Power BI Desktop completely.
3. Open your terminal in VS Code (or your code editor) in the `Chess-Power-BI-Dashboard-Repo` folder.
4. Run the following commands to save your incredible work to GitHub:
   ```bash
   git add .
   git commit -m "feat: Completed full Power BI dashboard integration with Star Schema and custom UI"
   git push origin main
   ```

🎉 **Congratulations!** Your enterprise-grade analytics portfolio project is officially complete and live on GitHub.
