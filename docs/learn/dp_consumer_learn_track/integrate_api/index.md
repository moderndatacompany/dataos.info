# Integration with data API

In this topic, you will learn how to use the Data Product via REST API. This guide offers step-by-step instructions for accessing and integrating the Data Product through REST API.

## Scenario

Considering that the 'Product360' Data Product fully meets your use case needs, you will now build a data application that generates valuable insights for the marketing team. These insights will empower them to create personalized promotions, enhance customer engagement, and drive additional business growth.

## Quick concepts

Before diving into the detailed steps, let’s cover some key concepts that will help you grasp the essentials:

- **Data API:** An interface that allows applications to programmatically access and manipulate data stored in a database or Data Product, enabling seamless integration and interaction.

## What do you need to get started?

To make the most of this guide, ensure you have:

- Familiarity with REST APIs and app development fundamentals.
- A DataOS API key with access to your Product 360 Data Product.

## Steps to follow

Follow these steps to access and consume the Data Product using the REST API:

1. **Navigate to the Access Options Tab**
    
    In the Data Product Hub, go to the **Access Options** tab, where you'll find the REST API endpoint for Product 360 Data Product.
    
    ![api_access.png](/learn/dp_consumer_learn_track/integrate_api/api_access.png)
    
2. **Copy the API Endpoint to Postman**
    
    Copy the endpoint URL provided, and open **Postman** (or your preferred API testing tool). Paste the URL into the request field.
    
    ![api_endpoint.png](/learn/dp_consumer_learn_track/integrate_api/api_endpoint.png)
    
3. **Authenticate with DataOS API Key**
    
    In Postman, go to the **Authorization** tab. Set the authorization type to **Bearer Token**, and enter your DataOS API key to authenticate.
    
    ![api_postman.png](/learn/dp_consumer_learn_track/integrate_api/api_postman.png)
    

4. **Send the request and view the output**
    
    After setting up your request, click **Send**. If configured correctly, you should see a successful API response, confirming that the endpoint and API key are working. This output is now ready to use in your data application.
    
    ![api_get.png](/learn/dp_consumer_learn_track/integrate_api/api_get.png)
    

## Next step

If you want to train machine learning models on your Data Product, proceed to the next module:

[Integration with AI/ML](/learn/dp_consumer_learn_track/integrate_aiml/)