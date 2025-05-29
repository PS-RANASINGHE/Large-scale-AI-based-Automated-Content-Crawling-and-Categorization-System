# Large-scale-AI-based-Automated-Content-Crawling-and-Categorization-System

## 🧾 Executive Abstract
This project was developed with the intention of simplifying the browsing experience for customers, particularly on shopping websites. Research indicates that an average person spends approximately 6 hours daily online. This is a significant issue, as theoretically, it might seem simple to reduce internet usage, but in practice, it’s not feasible. Even with the filters available on websites, users often end up spending excessive time searching for the optimal product. Recognizing that AI is increasingly being used to streamline daily tasks, the team aimed to alleviate this problem by developing an AI powered solution that handles the filtering and searching process, delivering near-optimal product recommendations for users. This project aspires to help customers save time spent on browsing and allow them to focus on more productive activities. The project primarily consists of two components: a model to generate outputs from crawled data and a database to store and train the model. 

## 🧠 The AI Model: Ollama
We chose Ollama, an open-source model capable of processing vast amounts of data and extracting meaningful patterns. It delivers precise recommendations tailored to individual user preferences. Ollama’s versatility simplifies the integration of large language models (LLMs) into various applications. Additionally, it allows for local hosting and customization, offering greater control over data privacy and reducing reliance on third-party services. The model also supports seamless model management, API interfaces, and cross-platform compatibility, making it an ideal choice for building custom AI solutions and experimenting with natural language interfaces. We utilized Ollama to extract specific attributes from product descriptions, as well as to translate Finnish to English for attributes like description, name, and categories.

## 🗄️ Database: MySQL Workbench and phpMyAdmin

The second key component of the project is the database. The team initially used SQL Workbench to design and manage the database with specific attributes. SQL Workbench provided a robust platform for creating and refining the initial relational database structure, ensuring efficient data handling. As the project progressed, the team transitioned to phpMyAdmin, an open-source web-based GUI tool, for ongoing database management. Due to the large volume of data, we used a Python script to convert the JSON data into CSV format, enabling easy import into the phpMyAdmin database. phpMyAdmin offers an intuitive interface for tasks such as table creation, query execution, and database monitoring. This combination of tools facilitated the efficient development and management of the database, supporting the project's complex requirements and enabling seamless integration with the AI model. Initially, the team ran the model on local computers. However, as the project progressed, it became clear that the available hardware resources were insufficient for handling the increasing computational demands. After discussions with the client, the team secured permission to use the high-performance computing resources provided by CSC at the university, specifically the CSC Mahti, as the Ollama model required high GPU capabilities. Deploying the model on CSC’s infrastructure allowed the team to achieve better outcomes and improve the efficiency of the project. 

## 📦 Deliverables and Outcome

The client required backend development and tasked the team with continuing an existing project to meet specific requirements. Initially, the project involved crawling minimal product ttributes from a few pages of the website. As the scope expanded, the team was asked to crawl data for the entire website, including more primary attributes. To enhance the crawling process, the team employed the AI model, Ollama 3.2, to extract more specific attributes from product descriptions. 

Given the complexity and time consumption of crawling data, the client requested crawling 10 products from each category to test the system. This also served to help identify subcategories within the main categories. The team initially planned to upgrade to Ollama 3.3 for improved performance, but this was not feasible due to time constraints and the limited resources available on Mahti, the high-performance computing system. 

The final deliverables included: 
+ Crawled JSON file with primary attributes using BeautifulSoup (bs4) and the requests library. 
+ Formatted CSV file with primary attributes from crawling and secondary attributes using Ollama 3.2. 
+ A comprehensive database used to train the model, ensuring the system could handle large volumes of data. 
+ The raw code used throughout the project. 

Ollama was scripted to accurately process the crawled data, specifically the product name and description, to provide tailored product-specific attributes. The project focused specifically on crawling data from www.tukku.net, adhering strictly to the client's specifications. 

In conclusion, the AI Content Crawling Project successfully developed a backend solution to train the LLM model. Despite challenges with computational resources, the team leveraged advanced AI models, a robust database system, and high-performance infrastructure to create a practical, efficient solution for e-commerce, improving the user experience significantly. 

## 🗂️ Project Structure

+ Website where data should be crawled: We crawl data from tukku.net, which is a shopping website with more than ten thousand data points.
+ Scripts to crawl and deal with data: We have scripts to crawl data and interact with Ollama to translate data and further generate attributes that are useful to return relevant products based on the user’s query. Also, the script exports a CSV file for later data cleaning work
+ Database to store cleaned data: The cleaned data will be stored in a database as one primary table and one wide table (columns that are most likely to be product related attributes like resistance).
+ Interface from customer’s side: This part is already implemented from the customer’s side, and our refined database could provide data to its API


![image](https://github.com/user-attachments/assets/74bb85cd-0df3-4ae6-88c4-efb30f505d63)

## 🔄 Workflow Diagram

![image](https://github.com/user-attachments/assets/1c741698-5ce1-418c-aec4-ffc88af054c2)

### 🛠️ Tools and Libraries

| Category    | Item                        |
|-------------|-----------------------------|
| Software    | Confluence (documentation)  |
| Software    | Jira (project management)   |
| Software    | GitHub (version control)    |
| Software    | CSC platform (Mahti)        |
| Software    | PyCharm (IDE)               |
| Software    | Visual Studio Code ,Jupyter Notebok          |
| Software    | Python (Programming language) |
| Software    | Ollama 3.2 (AI model)       |
| Software    | MySQL Workbench             |
| Software    | MySQL phpMyAdmin            |
| Dependency  | Illama 3.2                  |
| Dependency  | BeautifulSoup (Crawling library) |
| Dependency  | Pandas (Library)            |
| Dependency  | Regex (Library)             |




