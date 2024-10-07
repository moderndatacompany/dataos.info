# Recipe

In this section, we will explore a recipe to explore Data Product Hub.

## Problem Statement

John, a senior investment analyst at a finance company, aims to assess investor risk, evaluate company valuations, and identify high-potential companies for hedge fund portfolios. To achieve this, he will collaborate with Max, a data analyst, to create a comprehensive dashboard for corporate performance and hedge fund metrics, to optimize investment strategies and manage risk effectively. Following are the key areas that need to be highlighted:

1. **Performance by Industry and Sector:** Assess the performance of different industries and sectors to identify trends and areas for investment opportunities. 
2. **Top-Performing Companies:** Identify which companies are performing best in terms of key financial indicators.
3. **Revenue and Financial Impact Analysis:** Analyze revenue and financial metrics to understand the impact of each company on overall portfolio performance.
4. **Operational Efficiency Metrics:** Determine operational efficiency to gauge financial health and identify areas for operational improvements.
5. **Debt and Risk Analysis:** Compare companies based on their debt levels to manage investment risk and optimize portfolio allocation.
6. **Financial Growth Patterns:** Identify patterns in financial growth to uncover potential investment opportunities and refine strategies.
7. **Hedge Fund Metrics Overview:** Compare hedge fund metrics to optimize investment decisions and manage fund performance.
8. **Regional Performance Comparison:** Compare the performance of companies across different countries to identify regional trends and opportunities.
9. **Investor Risk Assessment:** Use financial metrics to assess and manage investor risk within the portfolio.

The goal is to enhance their ability to assess corporate performance, manage hedge fund metrics, and optimize investment strategies, leading to improved decision-making and portfolio performance.

## Discovering a Data Product

To solve the problem, Max uses the Data Product Hub, a Graphical User Interface within DataOS where data analysts can discover actionable [Data Products](/products/data_product/). Max follows the steps below to identify the potential Data Products to solve his use case.

1. To get started with the Data Product Hub, Max clicks on the **Data Product Hub 2.0** within the DataOS User Interface.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(1).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    <figcaption><i>DataOS User Interface</i></figcaption>
    </center>


2. Max is redirected to the Data Product Hub home page after login, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(2).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    <figcaption><i>Data Product Hub Home Page</i></figcaption>
    </center>  


3. The home page consists of Data Product recommendations based on the use case by default, but Max wants the Data Product recommendations of the ‘Corporate Finance’ domain, so he clicks on the **Filters** drop-down menu on the left side and selects the **Domain** option where he tick marks the ‘Corporate Finance’ option, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(3).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>  

4. Max gets recommendations for Data Products in the Corporate Finance domain as shown below, he discovers a relevant Data Product ‘Corp Market Performance’, which will help him to evaluate the stock market risks.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(4).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  

5. To solve his use case, **Max** also needs to identify high-potential companies for hedge fund portfolios, tracking key financial indicators, and operational efficiency. He has found this Data Product in the recommendations as well. The Data Product ‘Corp Performance’ provides critical insights into identifying high-potential companies for hedge fund portfolios, tracking key financial indicators, operational efficiency, and performance metrics.

6. Max now started exploring the ‘Corp Market Performance’ Data Product. He first clicks on the ‘Corp Market Performance’ Data Product which will open an interface where he can see all the details of this specific Data Product as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(5).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  


7. Max explores each tab, in the **Overview tab,** he gets the details on the lineage of the Data Product to find the origin of the Data Product with **Inputs** which shows all the input datasets fed into the Data Product, **Outputs** which shows all the datasets generated from the Data Product, **Access options** which show the various options through which the Data Product can be consumed, **Models** which show various lens models that are consuming the Data Product. 
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(6).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
      
8. In the **Input tabs,** he explores the input datasets in detail. It provides him with a short description of the dataset, its tier, domain, owner, restricted access depending on the policy applied, the DataOS address of the dataset, and the Data Products in which the input dataset is used as input, as shown below. 
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(7).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
    He also, search the columns by name in the search bar as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(8).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>  
      
9. Below the search bar, he has the information about each column in a tabular format where he has details about the data types of each column as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(9).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
10. Similarly, Max explored the Output tab where he can see the details of the output dataset named `market_data` generated by the Data Product to see if he has all the necessary dimensions and measures available for his use case.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(11).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
11. Max finds two dimensions, `marketid`and `companyid` and a few measures, `capitalexpenditures`, `shareholdersequity`, `marketpershare`, `equitypershare`, `dividendpershare`, `netincome`, and `net_profit_after_tax` that will help him with this use case.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(12).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
12. In the **Quality tab**, Max sees all the SLOs (Service Level Objectives) or quality checks applied to the output data, Freshness has 0% SLO adherence, Schema has 100% SLO adherence, Validity has 0% SLO adherence, completeness has 100% SLO adherence, Uniqueness has 0% SLO adherence, and Accuracy has 0% SLO adherence. Max continues further as the output data is complete and has the correct schema that will help him with his use case.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(13).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
    <aside class="callout">
    🗣 Service Level Objectives (SLOs) are our Data Product's defined data quality standards, ensuring it meets user expectations and business needs. We continuously monitor our Data Product against these SLOs using data quality checks to identify and address any deviations promptly. SLO Adherence indicates the success rate of data quality checks and can be calculated as `SLO Adherence (%) = (Total Checks Passed / Total Checks Applied) * 100`.
    </aside>
    
13. In the **Access Options tab**, Max sees all the options through which he can consume this Data Product, he found the option **Tableau Cloud** is helpful for dashboard creation.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(14).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
14. But before that, Max wants to explore this Data Product further by clicking on the **Explore button** in the right corner as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(49).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>  
    

15. **The Explore button** will open a studio interface as shown below, where Max can explore the iris board which he examines, by clicking on the `market_data`, measures like `price_to_earnings_ratio`, `return_on_equity_ratio`, `earnings_per_share`, and `dividend_yield_ratio` to evaluate how well companies are performing. This helps him in assessing profitability, valuation, and return on investment. To use the iris board efficiently, Max clicked on the `price_to_earnings_ratio` measure and `company_id` as a dimension which will be reflected on the Members tab, on clicking the `Run Query` button on the right side he can examine the table then he clicked the **Chart tab** to ****visualize the data points as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(16).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(17).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
       
16. Max further explored to:
    - Examine `dividend_per_share`, `total_dividend_per_share`, and `earnings_per_share` to understand the company's profitability and its policy on dividend distribution.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(18).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - Analyze `total_shareholders_equity` to understand the overall financial health and stability of the company.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(19).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - Examine `total_market_per_share`, `marketpershare`, and `total_dividend_per_share` to gauge how the company's shares are performing in the market.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(20).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - Examine `total_net_income` and `total_net_profit_after_tax` to determine the overall profitability and efficiency of the company. This is crucial for evaluating how well the company converts revenue into profit.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(21).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - Analyze `shareholdersequity`, `capitalexpenditures`, and `total_debt_hid` to understand how effectively the company is managing its capital and investments.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(22).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - Analyze ratios `debt_equity_ratio` and `equity_multiplier` to assess financial risk and stability. High leverage or poor ratios could indicate potential risk areas.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(23).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
             
17. Max bookmarked the Data Product to favorites to get daily updates as he will be using this Data Product for his use case. He can later find the bookmarked Data Products in the Favorites tab in the **Data Products tab** as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(25).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
18. Similarly, Max also explores the ‘Corp Performance’ Data Product as this one also helps with his use case. He finds all the necessary measures and dimensions required for his use case.

## Activating the Data Product via BI Sync

Then he goes back to the ‘Corp Market Performance’ Data Product to share it with Tableau.

Max followed the below steps to share the Data Product with Tableau:

1. He goes to the **Access Options tab** and finds the option of Tableau Cloud under the BI Sync section as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(26).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
2. Then he clicked on the **Add connection** where he needed to provide Tableau Cloud credentials such as Project Name, Server Name, Site Id, Username, and Password. 
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(27).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>  
        
3. After giving the required credentials, Max clicked on the **Activate** button, which will activate the Data Product which means now Max can consume this Data Product on Tableau Cloud to create Dashboard. This step will create a new project in Tableau Cloud named ‘Corporate finance’.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(28).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>  
        

## Consuming the Data Product on Tableau Cloud

After successfully activating all the required Data Products, Max is ready to create the dashboard on Tableau Cloud. Let’s see how he initialized dashboard creation in the Tableau cloud with the following steps:

1. Max logged in to Tableau Cloud using his Tableau Cloud username and password which he provided while activating the Data Products, then he was redirected to the Tableau Cloud home page as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(29).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        

2. He clicked on the **Manage Projects** option on the home page as shown below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(30).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>  
        
3. **The Manage Projects** option will open an interface where Max finds all the projects he has worked on, where he also finds the newly created project ‘Corporate finance’ as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(31).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
4. He clicked on the ‘Corporate finance’ project, where he could see the data sources that he can consume to create the dashboard.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(32).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
5. Then he clicked on the menu option at the right corner of the data source and selected the **New Workbook** option as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(33).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
6. To create a new workbook, Max was asked to provide his DataOS username and API key as the password to sign in to the data source to open the view.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(34).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>  
        
7. After signing in, he is redirected to the workbook where he can start creating the dashboard.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(35).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        

## Exploring the Data Product

After successfully setting up the dashboard with the relevant data products, Max wants to take the analysis one step further by adding forecasting capabilities to predict future trends for their hedge fund portfolio. This will help John make informed investment decisions and anticipate potential risks. for which Max followed the below steps:

1. Max goes back to the Data Product Hub and continues his data analysis journey, by clicking on the ‘Explore’ button an interface will open where he can perform cross Data Product analysis and determine if he has enough data to build a forecast model.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(36).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
    - Max begins by comparing the **Corp Market Performance** and **Corp Performance** data products to analyze how companies perform across different **industries and sectors**. He focuses on metrics like **net income**, **revenue growth**, and **operational efficiency** to understand which companies in various sectors are delivering the strongest financial results.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(37).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - He filters the data to focus on specific sectors such as ‘Financial Services’, identifying the companies with the highest **earnings per share** and **net income**. This helps him narrow down high-performing companies that should be prioritized for hedge fund allocation.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(38).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
    - Max saves his exploration as a perspective as he will need to revisit these insights more often for his use case. He clicked on the Save Perspective option as shown below.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(39).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
        </center>  
        
2. To save the perspective, Max has to provide the name and description of his exploration so that he can revisit these insights later.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(40).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
3. To revisit the perspective, Max has to navigate to the Perspectives tab as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(41).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>  
        
4. In the Perspective tab, he searched for his saved perspective by name as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(42).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
5. On clicking the perspective, Max is redirected to the Explore interface where he can access all the perspectives created on the Data Product along with his own.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(43).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        

## Activating the Data Product via Jupyter Notebook

Now after exploring the Data Product, Max is ready to build models, for which he needs to activate the Data Product via Jupyter Notebook, to do so he followed the below steps:

1. He goes back to the ‘Corp Market Performance’ Data Product and navigates to the Access Options tab, in the AI and ML section he clicks on the Download, which downloads a `.ipynb` file.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(44).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
2. Max opens the .`ipynb` file with Visual Studio as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(45).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>  
        
3. He chooses to go with REST API templates. Which looks like the following.
    - REST API template
        
        ```python
        # Import necessary libraries
        import requests
        import pandas as pd
        import json
        
        # API URL and API key
        api_url = "https://lucky-possum.dataos.app/lens2/api/public:company-intelligence/v2/load"
        apikey = 'api key here'
        
        # API payload, enter YOUR_QUERY here.
        payload = json.dumps({
            "query": {
                YOUR_QUERY
            }
        })
        
        # Query Example: This is how your query should look like.
        
            # "query": {
            #     "measures": [
            #         "sales.total_quantities_sold", 
            #         "sales.proof_revenue"
            #     ],
            #     "dimensions": [
            #         "inventory.warehouse"
            #     ],
            #     "timeDimensions": [
            #         {
            #             "dimension": "sales.invoice_date",
            #             "granularity": "day"
            #         }
            #     ],
            #     "limit": 1000,
            #     "responseFormat": "compact"
            # }
        
        # Headers
        headers = {
            'Content-Type': 'application/json',
            'apikey': apikey
        }
        
        # Fetch data from API
        def fetch_data_from_api(api_url, payload, headers=None):
            response = requests.post(api_url, headers=headers, data=payload)
            
            if response.status_code == 200:
                data = response.json()
                df = pd.json_normalize(data['data'])  # Create DataFrame
                return df
            else:
                print(f"Error: {response.status_code}")
                return None
        
        # Main execution
        if __name__ == "__main__":
            data = fetch_data_from_api(api_url, payload, headers=headers)
            
            if data is not None:
                print("Data Frame Created:")
                print(data.head())  # Show the first few rows of the DataFrame
                print("Ready for AI/ML model building.")
            else:
                print("Failed to fetch data.")
        
        ```
        
4. In the template, Max got to know that he needed to provide the API URL as api_url and the DataOS API key as apikey for which in DPH he navigated to the Data APIs section from where he downloaded the Postman collection and OpenAPI specification to explore and test the API endpoint.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(46).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
5. Max opened the Postman application and imported the Postman collection to test the API endpoint.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(47).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>  
        
 
        
6. He copied the base URL, pasted it in place of {{baseUrl}}, provided his DataOS API key as a bearer token, and clicked Send. He found out that the API endpoint was working fine.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(48).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center> 

7. Now he provided the API URL and API key on the REST API template and executed the code. Max is ready to build a Forecasting model.

8. Then Max requested **Eric, the Data Product owner** to include columns related to forecasting in the 'Corp Performance' data product.

Through his thorough exploration and utilization of Data Product Hub within DataOS, Max successfully discovers and activates relevant data products like **Corp Market Performance** and **Corp Performance**. By leveraging these Data Products, he provides John, the senior investment analyst, with key insights into corporate performance, industry trends, and operational efficiency, enabling data-driven decision-making for hedge fund strategies.

Max's ability to integrate data with Tableau Cloud for seamless dashboard creation and his use of Jupyter Notebook to build forecasting models demonstrate how effectively DataOS empowers data analysts to manage complex financial use cases. With the added collaboration from the Data Product owner, Eric, to incorporate additional forecasting columns, Max ensures that John’s hedge fund strategies are optimized for future growth and risk mitigation.