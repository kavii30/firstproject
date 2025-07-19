

from movies import recommend

if __name__ == "__main__":
    movie_name = input("Enter a movie name: ").strip()
    recommendations = recommend(movie_name)

    print("\nRecommended movies:")
    for movie in recommendations:
        print("🎬", movie)
