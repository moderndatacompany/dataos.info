# Example

In this section, a real-life use case is explained to demonstrate how Data Product Hub can be utilized.

## Problem statement

John, a senior investment analyst at a finance company, aims to assess investor risk, evaluate company valuations, and identify high-potential companies for hedge fund portfolios. To achieve this, collaboration will take place with Max, a data analyst, to develop a comprehensive dashboard for corporate performance and hedge fund metrics, designed to optimize investment strategies and manage risk effectively. The key areas to be highlighted are as follows:

1. Performance by Industry and Sector: The performance of different industries and sectors will be assessed to identify trends and areas for investment opportunities.
2. Top-Performing Companies: Companies will be identified based on their performance using key financial indicators.
3. Revenue and Financial Impact Analysis: Revenue and financial metrics will be analyzed to determine their impact on overall portfolio performance.
4. Operational Efficiency Metrics: Operational efficiency will be measured to assess financial health and identify areas for operational improvements.
5. Debt and Risk Analysis: Companies will be compared based on their debt levels to manage investment risk and optimize portfolio allocation.
6. Financial Growth Patterns: Financial growth patterns will be identified to uncover potential investment opportunities and refine strategies.
7. Hedge Fund Metrics Overview: Hedge fund metrics will be compared to optimize investment decisions and manage fund performance.
8. Regional Performance Comparison: The performance of companies across different countries will be compared to identify regional trends and opportunities.
9. Investor Risk Assessment: Financial metrics will be used to assess and manage investor risk within the portfolio.

The goal is to enhance the ability to assess corporate performance, manage hedge fund metrics, and optimize investment strategies, leading to improved decision-making and portfolio performance.


## Discovering a Data Product

To address the problem, the Data Product Hub, a graphical user interface within DataOS, is utilized by Max, a data analyst. This platform allows data analysts to discover actionable [Data Products](/products/data_product/). The steps below are followed to identify relevant Data Products for solving the use case.

1. The Data Product Hub 2.0 is accessed within the DataOS user interface to begin exploring the Data Product Hub.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>DataOS User Interface</i></figcaption>
    </center>

2. After login, it redirected to the Data Product Hub home page, as displayed below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Data Product Hub Home Page</i></figcaption>
    </center>

3. By default, Data Product recommendations are displayed based on the use case. However, to find Data Products in the 'Corporate Finance' domain, the Filters drop-down menu is accessed. The Domain option is selected, and 'Corporate Finance' is chosen, as shown below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(3).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>

4. Recommendations for Data Products within the Corporate Finance domain are displayed. The 'Corp Market Performance' Data Product is identified as relevant for evaluating stock market risks.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(4).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

5. The 'Corp Performance' Data Product is also found in the recommendations. This Data Product assists in identifying high-potential companies for hedge fund portfolios, tracking key financial indicators, and monitoring operational efficiency.

6. The 'Corp Market Performance' Data Product is selected for further exploration. This opens an interface where all details of the specific Data Product are displayed, as shown below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(5).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

7. Each tab of the Data Product is examined. In the Overview tab, the lineage of the Data Product is reviewed, including Inputs (input datasets), Outputs (datasets generated from the Data Product), Access options (ways the Data Product can be consumed), and Models (lens models consuming the Data Product).

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(6).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

8. The Input tab is used to explore input datasets in detail, providing a description of the dataset, its tier, domain, owner, and access restrictions, along with the DataOS address and other related Data Products.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(7).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

    Dataset columns can be searched by name using the search bar, as shown below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(8).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>

9. Information about each column is provided in a tabular format, including data types of each column, as displayed below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(9).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

10. The Output tab is explored to examine the output dataset named `market_data`, ensuring all necessary dimensions and measures are available for the use case.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(11).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

11. Two dimensions, `marketid` and `companyid`, are identified along with measures such as `capitalexpenditures`, `shareholdersequity`, `marketpershare`, `equitypershare`, `dividendpershare`, `netincome`, and `net_profit_after_tax`, which will assist with the use case.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(12).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

12. In the Quality tab, Service Level Objectives (SLOs) are reviewed, including adherence levels for freshness, schema, validity, completeness, uniqueness, and accuracy. Despite some SLOs having 0% adherence, the output data is determined to be complete with the correct schema.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(13).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

    <aside class="callout">
    🗣 Service Level Objectives (SLOs) are the defined data quality standards for the Data Product, ensuring alignment with user expectations and business needs. Continuous monitoring of the Data Product is conducted against these SLOs using data quality checks to promptly identify and address any deviations. SLO adherence represents the success rate of these data quality checks and is calculated as SLO Adherence (%) = (Total Checks Passed / Total Checks Applied) * 100.
    </aside>

13. In the Access Options tab, various options for consuming the Data Product are reviewed. The Tableau Cloud option is identified as useful for dashboard creation.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(14).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

14. Before consuming the Data Product, Max clicks on the Explore button in the top-right corner to further examine it.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(49).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>

15. Clicking the Explore button opens a studio interface. Within this interface, Max explores the iris board. For this use case, the `price_to_earnings_ratio` measure and `company_id` dimension are selected. The Run Query button is clicked to examine the table, followed by clicking the Chart tab to visualize the data points.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(16).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(17).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

16. Additional exploration includes:
    - Analyzing `dividend_per_share`, `total_dividend_per_share`, and `earnings_per_share` to assess profitability and dividend distribution policies.

        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(18).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>

    - Examining `total_shareholders_equity` to evaluate the financial health and stability of the company.

        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(19).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>

    - Exploring `total_market_per_share`, `marketpershare`, and `total_dividend_per_share` to gauge stock performance.

        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(20).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>

    - Investigating `total_net_income` and `total_net_profit_after_tax` to measure profitability and efficiency.

        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(21).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>

    - Analyzing `shareholdersequity`, `capitalexpenditures`, and `total_debt_hid` to assess capital management.

        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(22).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>

    - Examining the `debt_equity_ratio` and `equity_multiplier` to evaluate financial risk and stability.

        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(23).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>

17. The Data Product is bookmarked for daily updates. Bookmarked Data Products can be accessed later from the Favorites tab in the Data Products section.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(25).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>

18. Similarly, the ‘Corp Performance’ Data Product is explored. All necessary measures and dimensions required for the use case are identified.


## Activating the Data Product via BI Sync

The ‘Corp Market Performance’ Data Product is returned to in order to share it with Tableau.

The steps below are followed to share the Data Product with Tableau:

1. The Access Options tab is navigated to, where the Tableau Cloud option is found under the BI Sync section, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(26).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
2. The Add connection button is selected, where Tableau Cloud credentials such as Project Name, Server Name, Site Id, Username, and Password are required. 
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(27).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>  
        
3. After the credentials are provided, the Activate button is selected. This activates the Data Product, allowing it to be consumed on Tableau Cloud for dashboard creation. A new project in Tableau Cloud is created, named ‘Corporate finance’.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(28).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>  

## Consuming the Data Product on Tableau Cloud

Once the required Data Products are activated, the dashboard on Tableau Cloud is created by following these steps:

1. Tableau Cloud is logged into using the previously provided credentials, and the user is redirected to the Tableau Cloud home page, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(29).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
2. The Manage Projects option on the home page is selected, as shown below.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(30).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>  
        
3. The Manage Projects option opens an interface where all projects, including the newly created ‘Corporate finance’ project, are listed, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(31).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
4. The ‘Corporate finance’ project is selected, displaying the data sources available for dashboard creation.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(32).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
5. The menu option in the top-right corner of the data source is selected, followed by the New Workbook option, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(33).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
6. To create a new workbook, the DataOS username and API key are provided as the password to sign in to the data source.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(34).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>  
        
7. After signing in, redirection to the workbook occurs, allowing the dashboard to be created.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(35).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  

## Exploring the Data Product

With the dashboard setup completed, the next step involves adding forecasting capabilities to predict future trends for the hedge fund portfolio. This assists in making informed investment decisions and anticipating risks. The following steps are taken:

1. The Data Product Hub is revisited, and the Explore button is selected, opening an interface to perform cross Data Product analysis. This analysis helps determine if enough data is available to build a forecast model.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(36).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  

    - The Corp Market Performance and Corp Performance Data Products are compared to analyze company performance across different industries and sectors. Focus is placed on metrics like net income, revenue growth, and operational efficiency to assess which companies in various sectors deliver the strongest financial results.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(37).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>  
        
    - Data is filtered to focus on sectors such as ‘Financial Services’, identifying companies with the highest earnings per share and net income, narrowing down high-performing companies for hedge fund allocation.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(38).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>  
        
    - The exploration is saved as a perspective, ensuring that these insights can be revisited frequently. The Save Perspective option is selected, as shown below.
        
        <center>
        <img src="/interfaces/data_product_hub/recipe/image%20(39).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
        </center>  

2. To save the perspective, a name and description of the exploration are provided for future reference.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(40).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  

3. The saved perspective is accessed by navigating to the Perspectives tab, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(41).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>  

4. The perspective is searched by name within the Perspectives tab, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(42).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  

5. Selecting the perspective redirects to the Explore interface, where all perspectives created on the Data Product, including the saved one, can be accessed.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(43).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  

## Activating the Data Product via Jupyter Notebook

Once the Data Product is explored, the next step is to build models. The Data Product is activated via Jupyter Notebook by following these steps:

1. The Corp Market Performance Data Product is navigated to, and the Access Options tab is accessed. In the AI and ML section, the Download button is selected, downloading a `.ipynb` file.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(44).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  

2. The `.ipynb` file is opened using Visual Studio, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(45).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    </center>  

3. The REST API template is selected, which appears as follows:

    - REST API template:
        
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
        
        # Headers
        headers = {
            'Content-Type': 'application/json',
            'apikey': apikey
        }

        # Fetch data from API
        def fetch_data_from_api(api_url, payload, headers=None):
            response is = requests.post(api_url, headers=headers, data=payload)
            
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




        
4. In the template, it is determined that the API URL must be provided as `api_url` and the DataOS API key as `apikey`. To retrieve these, the Data APIs section in DPH is navigated, where the Postman collection and OpenAPI specification are downloaded to explore and test the API endpoint.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(46).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
5. The Postman application is opened, and the Postman collection is imported to test the API endpoint.
    
    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(47).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center>  
        
6. The base URL is copied, pasted in place of `{{baseUrl}}`, and the DataOS API key is provided as a bearer token. The Send button is selected, confirming that the API endpoint is functioning correctly.

    <center>
    <img src="/interfaces/data_product_hub/recipe/image%20(48).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    </center> 

7. The API URL and API key are provided in the REST API template, and the code is executed. The system is now ready to build a forecasting model.

8. A request is made to Eric, the Data Product owner, to include columns related to forecasting in the 'Corp Performance' data product.

Through a thorough exploration and utilization of the Data Product Hub within DataOS, relevant Data Products such as Corp Market Performance and Corp Performance are successfully discovered and activated. By leveraging these Data Products, key insights into corporate performance, industry trends, and operational efficiency are provided to John, the senior investment analyst, enabling data-driven decision-making for hedge fund strategies.

The seamless integration of data with Tableau Cloud for dashboard creation and the use of Jupyter Notebook to build forecasting models demonstrate how effectively DataOS supports data analysts in managing complex financial use cases. With the collaboration from the Data Product owner, Eric, to include additional forecasting columns, the hedge fund strategies are optimized for future growth and risk mitigation.
