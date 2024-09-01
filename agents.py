from crewai import Agent
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool
import os
os.environ['GROQ_API_KEY']='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'
os.environ["SERPER_API_KEY"]="790c841615ee76a54f3d62cc3dc9eb611d0397bc"
serper=SerperDevTool()
web_scrape=ScrapeWebsiteTool()

llm=ChatGroq(
    temperature=0.9,
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama3-8b-8192",
)
class trichyagents():
    def holy_places(self):
        return Agent(
            role="holy place Finder",
            goal="To find the holy places efficiently",
            backstory="find the places  which are famous and it should search for the church,temple,mosque ",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    def jewellery_shop(self):
        return Agent(
            role="Jewellery Shop Finder",
            goal="To find the Jewellery shop places efficiently",
            backstory="find only the places  which are famous ",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    def shopping_mart(self):
        return Agent(
            role="Shopping Mart Finder",
            goal="To find the shopping mart places efficiently",
            backstory="find only the places  which are famous and used by many people ",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    def courier_service(self):
        return Agent(
            role="courier service seacher",
            goal="To find the courier service places efficiently",
            backstory="find only the places  which are used by many people ,it should be safe and secure",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    def restaurant_analyst(self):
        return Agent(
           role = "Restaurant Suggestor",
           goal = "To provide the names of the best restaurants in {city}"
                   "also give the exact location of the restaurant"
                   "also mention what are the restaurant best selling or special dishes",
            backstory = "you are a expert in suggesting restaurants"
                "you know every restaurant in {city}"
                
                ,
             verbose = True,
            max_iter = 15,
            allow_delegation=False,
            tools = [serper],
            llm = llm
)

    def servicecenter_finder(self):
        return Agent(
    role = "Service Center Locator",
    goal = "To provide the names of the best automobile service centers in the {city}"
    "also give the exact location of the automobile service centers"
    "also mention the exact address of the automobile service centers",
    backstory = "you are a expert in locating automobile service centers"
                "you know every automobile service center in {city}"
                "also provide what is the opening time and closing time"
                
                ,
    verbose = True,
    max_iter = 15,
    tools = [serper],
    llm = llm
)

    def Homeapplst_finder(self):
        return Agent(
    role = "Home Appliances store Locator",
    goal = "To provide the names of the best Home Appliances Stores in the {city}"
    "also give the exact location of the Home Appliances Stores"
    "also mention the exact address of the Home Appliances Stores",
    backstory = "you are a expert in locating Home Appliances Stores"
                "you know every Home Appliances Store in {city}"
                "also provide what is the opening time and closing time"
                
                ,
    verbose = True,
    max_iter = 24,
    allow_delegation=False,
    tools = [serper],
    llm = llm
)  
    def entertainment_agent(self):
        return Agent(
            role="Entertainment Finder",
            goal=" by using the tool Locate parks and theaters efficiently in {city}",
            backstory="Find only the most popular and highly positive rated theaters in {city}"
                       " highly positive rated parks in {city}",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

    def vessel_shop_agent(self):
        return Agent(
            role="Vessel Shop Finder",
            goal="Find shops specializing in kitchenware store in {city}",
            backstory="Identify trustworthy shops with a wide range of kitchenware options in {city} send the exact location of it with landmark",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ) 

    def stationary_shop_agent(self):
        return Agent(
            role="Stationary Shop Finder",
            goal="Locate shops selling stationary items in {city}",
            backstory="Find reputable stationary shops known for quality products located in {city} with landmark",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

    def photoshop_agent(self):
        return Agent(
            role="Photoshop Finder",
            goal="Find shops offering photo studio in that particular location {city} by using the tool",
            backstory="Locate reliable photo studio services with good customer reviews by using the tool for that particular location in {city}",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

    def hospital_analyst(self):
        return Agent(
    role = "hospitals Suggestor",
    goal = "To provide the names of the best hosipitals in {city}"
    "also give the exact location of the hospitals"
    "also mention what are the speacialised treatment in that hospitals",
    backstory = "you are a expert in suggesting hospitals"
                "you know every hospitals in {city}"
                
                ,
    verbose = True,
    max_iter = 15,
    allow_delegation=False,
    tools = [serper],
    llm = llm
)
    def companies(self):
        return Agent(
            role="companies",
            goal="To search companies that located in city.It can IT or Automobiles to the user",
            backstory="To search the companies that is located in city.It can be IT companies or Automobile Companies to suggest to the user. then show top companies in trichy then using the tools",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,
)
    def furniture_shop(self):
        return Agent(
            role="Furniture Shop",
            goal="To generate a furniture shop that should be near or located in city to the user",
            backstory="To generate a furniture shop that located in city to suggest top most furniture shops to the users , using the tools",
            tool=[serper],
            verbose=True,
            allow_delegation=False,
            llm=llm,

)
    def gift_shop(self):
            return Agent(
                 role="gift shop",
                 goal="To display the gift shops located in city to the user",
                 backstory="To display the gift shops located in city to suggest top most gift shops to the user , using the tool",
                 tool=[serper],
                 verbose=True,
                 allow_delegation=False,
                 llm=llm,

)

    def textile(self):
        return Agent(
            role="Find textile shops",
            goal="To find the textile shop places efficiently",
            backstory="""find only the places  which are famous
                       textile for both men and women and cloth quality is very important
                       you must use the tool for searching the details""",
            tool=[serper],
            allow_delegation=False,
            verbose=True,
            llm=llm
        )
    def Parlour(self):
        return Agent(
            role="Beauty parlour Shop Finder",
            goal="To find the beauty parlour shop places efficiently",
            backstory="""find only the places  which are famous
                       Beauty parlour for grooming and bridal makeup for both men and women
                       you must use the tool for searching the details""",
            tool=[serper],
            allow_delegation=False,
            verbose=True,
            llm=llm
        )
    def institute(self):
        return Agent(
            role='Institution seacher',
            goal='Find the schools and colleges',
            backstory='To find best school and college in trichy'
                       'you must use the tool for searching the details',
            tool=[serper],
            verbose=True,
            llm=llm
        )
    def tour(self):
        return Agent(
            role="Find tourist place",
            goal="To find the tourist places efficiently",
            backstory="""find only the places  which are famous
                       exact location of tourist place to the user
                       you must use the tool for searching the details""",
            tool=[serper],
            allow_delegation=False,
            verbose=True,
            llm=llm
        )

    def room_analyst(self):
        return Agent(
    role = "rooms Suggestor",
    goal = "To provide the names of the best rooms in {city}"
    "also give the exact location of the rooms",
    backstory = "you are a expert in suggesting rooms"
                "you know every rooms and best staying place in {city}"
                
                ,
    verbose = True,
    max_iter = 15,
    allow_delegation=False,
    tools = [serper],
    llm = llm
)
    
    