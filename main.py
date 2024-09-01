from crewai import Crew
from dotenv import load_dotenv
from agents import trichyagents
from tasks import trichytask

load_dotenv()

city=input("enter your city name:")

#assigning task and agent
agent=trichyagents()
task=trichytask()

#create agent
holy_places=agent.holy_places()
jewellery_shop=agent.jewellery_shop()
shopping_mart=agent.shopping_mart()
courier_service=agent.courier_service()
restaurant_analyst=agent.restaurant_analyst()
servicecenter_finder=agent.servicecenter_finder()
Homeapplst_finder=agent.Homeapplst_finder()
entertainment_agent=agent.entertainment_agent()
vessel_shop_agent=agent.entertainment_agent()
stationary_shop_agent=agent.stationary_shop_agent()
photoshop_agent=agent.photoshop_agent()
hospital_analyst=agent.hospital_analyst()
companies=agent.companies()
furniture_shop=agent.furniture_shop()
gift_shop=agent.gift_shop()
textile=agent.textile()
parlour=agent.Parlour()
institute=agent.institute()
tour=agent.tour()
room_analyst=agent.room_analyst()

#create task
holy_place_searcher=task.holy_place_searcher(holy_places)
Jewellery_finder=task.Jewellery_finder(jewellery_shop)
mart_seracher=task.mart_seracher(shopping_mart)
courier_finder=task.courier_finder(courier_service)
restaurant_suggest=task.restaurant_suggest(restaurant_analyst)
suggest_auto=task.suggest_auto(servicecenter_finder)
suggest_homeappl=task.suggest_homeappl(Homeapplst_finder)
entertainment_task=task.entertainment_task(entertainment_agent)
vessel_shop_task=task.vessel_shop_task(vessel_shop_agent)
stationary_shop_task=task.stationary_shop_task(stationary_shop_agent)
photoshop_task=task.photoshop_task(photoshop_agent)
hospital_suggester=task.hospital_suggester(hospital_analyst)
finding_IT_companies=task.finding_IT_companies(companies)
finding_Automobiles_companies=task.finding_Automobiles_companies(companies)
locating_display_furniture=task.locating_display_furniture(furniture_shop)
discovering_gift_shops=task.discovering_gift_shops(gift_shop)
text_task=task.text_task(textile)
par_task=task.par_task(parlour)
skl_task=task.skl_task(institute)
clg_task=task.clg_task(institute)
tour_task=task.tour_task(tour)
stay_suggest=task.stay_suggest(room_analyst)

crew=Crew(
    agents=[
        holy_places,
        jewellery_shop,
        shopping_mart,
        courier_service,
        restaurant_analyst,
        servicecenter_finder,
        Homeapplst_finder,
        entertainment_agent,
        vessel_shop_agent,
        stationary_shop_agent,
        photoshop_agent,
        hospital_analyst,
        companies,
        furniture_shop,
        gift_shop,
        textile,
        parlour,
        institute,
        tour,
        room_analyst

    ],
    tasks=[
        holy_place_searcher,
        Jewellery_finder,
        mart_seracher,
        courier_finder,
        restaurant_suggest,
        suggest_auto,
        suggest_homeappl,
        entertainment_task,
        vessel_shop_task,
        stationary_shop_task,
        photoshop_task,
        hospital_suggester,
        finding_IT_companies,
        finding_Automobiles_companies,
        locating_display_furniture,
        discovering_gift_shops,
        text_task,
        par_task,
        skl_task,
        clg_task,
        tour_task,
        stay_suggest

    ],
    verbose=2
)

result=crew.kickoff(inputs={"city":city})
print(city)