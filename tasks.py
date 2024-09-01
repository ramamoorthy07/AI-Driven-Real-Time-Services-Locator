from crewai import Task
class trichytask():
    def holy_place_searcher(self,agent):
        return Task(description="""The holy places, known for their spiritual significance and historical importance, should be within {city}. Display the rate of visitor satisfaction and use the tool to search for these locations. If the tool has been used, print the used tool.""" ,
                    expected_output="""The holy places, including churches, temples, and mosques, should be within {city}. Display their precise names, addresses, and ratings.""",
                    agent=agent,)
    def Jewellery_finder(self,agent):
        return Task(description="""The jewelry shop must be a trustworthy shop with traditional craftsmanship and high-quality pieces. It should be within {city}. Use the tool to search for reputable jewelry shops in the area. If the tool has been used, print the used tool.""" ,
                    expected_output="""The jewellery shop must offer gold, diamond, and platinum jewellery and should be within {city}. Display its exact name, address, and rating.""",
                    agent=agent,)
    def mart_seracher(self,agent):
        return Task(description="""The shopping mart, known for its wide variety of products and popularity among locals, must be used by many people and should be within {city}. Use the tool to search for well-frequented shopping marts. If the tool has been used, print the used tool.""" ,
                    expected_output="""The shop must offer a wide range of products, including groceries, and should be within {city}. Display its precise name, address, and rating.""",
                    agent=agent,)
    def courier_finder(self,agent):
        return Task(description="""The courier service must offer reliable worldwide delivery and should have an office within {city}. Use the tool to search for globally recognized courier services. If the tool has been used, print the used tool.""" ,
                    expected_output="""Display the precise names, addresses, and ratings of courier services within {city}, along with details of their services.""",
                    agent=agent)

    def restaurant_suggest(self,agent):
      return Task(
    description = "In this you have to surf through the internet with the tools provided to you, and search for the best restaurants in {city}",
    expected_output = "Top Restaurants with their location and menu"
    "Location of the restaurant is very important"
    "Location should be very detailed"
    "also give some reviews about restaurant"
    "also provide what are the restaurant's famous dishes",
    agent = agent,
    max_iter = 15,
)

    def suggest_auto(self,agent):
      return Task(
    description = "In this you have to surf through the internet with the tools provided to you, and search for the best automobile service centers in {city}",
    expected_output = "Top automobile service centers with their location and menu"
    "Location of the automobile service centers is very important"
    "Location should be very detailed and specific"
    "also give some reviews about automobile service centers "
    "also provide what is the opening time and closing time",
    agent = agent,
    max_iter = 15,
)

    def suggest_homeappl(self,agent):
      return Task(
    description = "In this you have to surf through the internet with the tools provided to you, and search for the best Home Appliances stores in {city}",
    expected_output = "Top Home Appliances stores with their location"
    "Location of the Home Appliances stores is very important"
    "Location should be very detailed and specific"
    "also give some reviews about Home Appliances stores "
    "also provide what is the opening time and closing time",
    agent = agent,
    max_iter = 24,
)


    def entertainment_task(self, agent):
        return Task(
            description="""Find popular parks and theaters in {city}.
              Use reliable sources to gather detailed information about each location. 
              Include details about attractions, amenities, and visitor experiences. 
              Provide the full, detailed addresses of each park and theater to ensure easy accessibility for users. 
              Focus on the most highly rated and frequently visited spots."""
              """tell which tool you refer""",
            expected_output="""A list of entertainment options including parks and theaters with detailed information such as location, attractions, and amenities."""
            """Display the contact details""",
            agent=agent
        )

    def vessel_shop_task(self, agent):
        return Task(
            description=""" Identify and locate top kitchenware shops in {city}. 
            Use reliable sources to gather comprehensive information about each store.
            Highlight the best shop based on reviews and variety of products offered. 
            Mention the types of kitchenware available, such as cookware, utensils, and specialty items. 
            Provide the full, detailed addresses for each shop."""
            """tell which tool you refer""",
            expected_output="""A list of vessel shops with detailed information such as shop name, location, and types of vessels sold."""
            """Display the contact details""",
            agent=agent
        )

    def stationary_shop_task(self, agent):
        return Task(
            description="""Search for reputable stationery shops in {city}.
                Use reliable sources to gather detailed information about each shop, including the range of products they offer.
                Highlight shops known for high-quality stationery items. 
                Provide the full, detailed addresses of each stationery shop to ensure easy access for customers. 
                Focus on the most popular and well-reviewed locations."""
                """tell which tool you refer""",
            expected_output="""A list of stationary shops with detailed information such as shop name, location, and types of stationary items sold."""
            """Display the contact details""",
            agent=agent
        )

    def photoshop_task(self, agent):
        return Task(
            description="""Locate photo studios and related services in {city}. 
            Use reliable sources to gather detailed information about each studio, including services offered and customer ratings.
            Highlight the studios with the best reviews and a wide range of services, such as portrait photography and photo printing.
             Provide the full, detailed addresses of each photo studio. """
             """tell which tool you refer""",
            expected_output="""A list of photoshop services with detailed information such as shop name, location, and services offered."""
            """Display the contact details""",
            agent=agent
        )

    def hospital_suggester(self,agent):
      return Task(
    description = "In this you have to surf through the internet with the tools provided to you, and search for the best hospitals in {city}",
    expected_output = "Top most hospitals with their location and treaments"
    "Location of the hospitals is very important"
    "Location should be very detailed and specific"
    "Location is very must"
    "also give some reviews about that hospitals"
    "also provide what are the hospital's treament",
    agent = agent,
    max_iter = 15,
)

    def finding_IT_companies(self,agent):
        return Task(
            description="To identifying and listing IT companies located in {city}. "
                         "The agent will use specialized tools to gather accurate and up-to-date information"
                         "from relevant sources. The objective is to provide users with detailed information"
                         "about various IT companies, including Comapnies names, locations, services offered, "
                         "and contact details.",
            expected_output="To show the exact location of IT Jobs to the user",
            agent=agent
            )
    def finding_Automobiles_companies(self,agent):
        return Task(
            description="identifying and listing Automobiles companies located in {city}." 
                        "The agent will use specialized tools to gather accurate and up-to-date information from relevant sources."
                        "The objective is to provide users with detailed information about various Automobiles companies, "
                        "including Companies names, locations, services offered, and contact details.",
            expected_output="To find the Automobiles Companies exact location  to the user",
            agent=agent
            )
    def  locating_display_furniture(self,agent):
        return Task(
            description= "Identify and list furniture shops located in {city} using the tool."
                          "Gather detailed information, including names, addresses, contact details, and types of furniture offered."
                          "Provide a selection of top furniture shops, ensuring accuracy and relevance."
                          "Include shop specialties, customer reviews, and unique features."
                           " the city will be "
                           " city:{city}",
            expected_output="To identify and display the furniture shops exactly location to the user ",
            agent=agent
            )
    def discovering_gift_shops(self,agent):
        return Task(
            description="Locate and list gift shops in {city} using the Tool."
                        "Gather information such as shop names, addresses, contact details, and types of gifts offered. "
                        "Provide a selection of top gift shops with relevant details for user convenience.",
            expected_output="To discovering the gift shops exactly located in {city}",
            agent=agent
        )

    def text_task(self,agent):
     return Task(
            description="""The textile shop must offer trustworthy and high-quality clothing suitable for both men and women. It should be located within {city} and cater to a wide range of clothing needs, from casual to formal wear. Use the designated tool to search for shops that meet these criteria. If the tool has been utilized, print the details of the tool used.""" ,
            expected_output="""In  textile shop cloths must be available for both men and women.Show only best shops only""",
            agent=agent,
            
        )
    def par_task(self,agent):
     return Task(
            description="""The beauty parlour must be a trustworthy establishment that offers services for both men and women. It should be located within {city} and provide a wide range of beauty treatments. Use the designated tool to search for parlours that meet these criteria. If the tool has been used, print the details of the tool used.""" ,
            expected_output="""the Beauty parlour shop must be gromming for both men and women""",
            agent=agent,
            
        )
    def skl_task(self,agent):
     return Task(
            description="""To find best school{city}
                         School should be in three boards.They are matriculation,CBSE,ICSE.The result should be shown for mentioned board only 
                         display only top school 
                         You must use the  tool and print the used tool.""",
            expected_output='''Diaplay detail of school''',
            agent=agent,
        )
    def clg_task(self,agent):
     return Task(
            description="""To find best college in {city}.College should be divided into three categories .They are arts and science,enginnering and polytechnic.The result should be shown for any one of user input
                        display only top school in {city}
                        You must use the mentioned tool.""",
            expected_output="""Diaplay detail of school or college""",
            agent=agent,
        )
    def tour_task(self,agent):
     return Task(
            description="""the tourist place was very familiar on {city} and the tourist place should be within the {city} and use the tool to search, if the tool has been used then print the used tool""" ,
            expected_output="""Tourist place name and address.Show only best tourist spot only""",
            agent=agent,
            
        )

    def stay_suggest(self,agent):
      return Task(
    description = "In this you have to surf through the internet with the tools provided to you, and search for the best rooms in {city}",
    expected_output = "Top most rooms with their location"
    "Location of the rooms is very important"
    "Location should be very detailed and specific"
    "Location is very must"
    "also give some reviews about that rooms",
    agent = agent,
    max_iter = 15,
)
