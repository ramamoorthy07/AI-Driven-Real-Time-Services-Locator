# Trichy Task Finder

**A comprehensive service-finding agent built with CrewAI that facilitates the discovery of various businesses and locations in a specified city, including holy places, shopping centers, and more.**

## Overview
Trichy Task Finder is a Python-based application leveraging the CrewAI framework to assist users in discovering various services and locations in the city of Trichy. The application encompasses multiple tasks aimed at searching for holy places, jewelry shops, shopping marts, hospitals, restaurants, and more. Each task utilizes a dedicated search methodology to ensure users receive accurate and relevant information tailored to their needs.

## Features
- **Holy Place Searcher**: Finds holy places based on spiritual and historical significance, providing visitor satisfaction ratings.
- **Jewelry Finder**: Locates reputable jewelry shops known for traditional craftsmanship and high-quality pieces.
- **Shopping Mart Search**: Identifies popular shopping marts frequented by locals, detailing product variety and ratings.
- **Courier Finder**: Searches for reliable courier services with global delivery options.
- **Restaurant Suggestions**: Recommends top restaurants along with their locations, menus, and reviews.
- **Automobile Service Centers**: Lists the best automobile service centers with detailed information.
- **Home Appliances Stores**: Finds reputable home appliances stores and their offerings.
- **Entertainment Options**: Discovers popular parks and theaters, detailing attractions and visitor experiences.
- **Vessel and Stationery Shops**: Locates top kitchenware and stationery shops based on product variety and reviews.
- **Hospital Suggestions**: Provides a list of the best hospitals and their treatment offerings.
- **Educational Institutions**: Searches for the best schools and colleges categorized by educational boards and types.
- **Tourist Attractions**: Identifies popular tourist spots within the city.

## Installation
To run this project, you'll need to have Python installed on your machine along with the CrewAI library. You can install the CrewAI library using pip:

```bash
pip install crewai
```

Clone this repository to your local machine:

```bash
git clone https://github.com/ramamoorthy07/AI-Driven-Real-Time-Services-Locator.git
cd AI-Driven-Real-Time-Services-Locator
```

## Usage
To use the task functionalities, instantiate the `trichytask` class and call the desired task method with the required agent parameter. For example:

```python
from crewai import Agent
from trichytask import trichytask

agent = Agent()
task_finder = trichytask()

# Searching for holy places in Trichy
holy_places_task = task_finder.holy_place_searcher(agent)
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- S. Ramamoorthy

## Future Enhancements
- **User Feedback Integration**: Collect user feedback to improve service recommendations.
- **Personalized Recommendations**: Implement personalized suggestions based on user preferences.
- **Mobile Application Development**: Create a mobile app for on-the-go access.
- **Multi-City Support**: Expand to support multiple cities for broader usage.
- **Integration with Mapping Services**: Provide navigation options through mapping services.
- **Enhanced Search Filters**: Add advanced filters for a better search experience.
- **Social Media Sharing**: Allow sharing of favorite places on social media.
- **Admin Dashboard**: Develop an admin panel for data management and analysis.
- **Localization**: Support multiple languages for diverse user groups.
- **Real-Time Updates**: Incorporate real-time information for accuracy.
