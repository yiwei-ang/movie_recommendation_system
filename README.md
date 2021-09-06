# Movie Recommendation System

The first commit is to:
* Data exploration, mining and visualization to rule out possible features.
* Initialize a content-based recommendation model using **consine similarity** which takes care of:
  * Director,
  * Top 3 Genres,
  * Top 3 Cast,
  * Top 3 Frequent Keywords.  

<!-- GETTING STARTED -->
## Getting Started

This is the instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/yiwei-ang/movie_recommendation_system.git
   ```
2. Build Docker image (Make sure you have Docker installed locally):
   ```sh
   cd movie_recommendation_system
   docker build -t {image_name} .
   ```
3. Run Jupyter in the Docker container:
   ```sh
   docker run -p 8888:8888 {image_name}
   ```
  
<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Your Name - [@Yiwei](https://www.linkedin.com/in/yiwei-ang-412bba138/) - mosesyiwei@gmail.com

Project Link: [https://github.com/yiwei-ang/movie_recommendation_system](https://github.com/yiwei-ang/movie_recommendation_system)
