import fresh_tomatoes
import media

hunger_games = media.Movie(
    "The Hunger Games",
    "Katniss Everdeen voluntarily takes her younger sister's place "
    "in the Hunger Games: a televised competition in which two teenagers "
    "from each of the twelve Districts of Panem are chosen at random "
    "to fight to the death.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://youtu.be/mfmrPu43DF8"
)

catching_fire = media.Movie(
    "The Hunger Games: Catching Fire",
    "Katniss Everdeen and Peeta Mellark become targets of the Capitol "
    "after their victory in the 74th Hunger Games sparks a rebellion "
    "in the Districts of Panem.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAyMjQ3OTAxMzNeQTJeQWpwZ15BbWU4MDU0NzA1MzAx._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://youtu.be/EAzGXqJSDJ8"
)

mockingjay_part1 = media.Movie(
    "The Hunger Games: Mockingjay - Part 1",
    "Katniss Everdeen is in District 13 after she shatters the games forever. "
    "Under the leadership of President Coin and the advice of "
    "her trusted friends, Katniss spreads her wings as she fights to save "
    "Peeta and a nation moved by her courage.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxNDI2NDAzNl5BMl5BanBnXkFtZTgwODM3MTc2MjE@._V1_SY1000_CR0,0,657,1000_AL_.jpg",
    "https://youtu.be/3PkkHsuMrho"
)

mockingjay_part2 = media.Movie(
    "The Hunger Games: Mockingjay - Part 2",
    "As the war of Panem escalates to the destruction of other districts, "
    "Katniss Everdeen, the reluctant leader of the rebellion, "
    "must bring together an army against President Snow, "
    "while all she holds dear hangs in the balance.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5BanBnXkFtZTgwNTAyMDQ5NjE@._V1_SY1000_CR0,0,657,1000_AL_.jpg",
    "https://youtu.be/KmYNkasYthg"
)

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt "
    "to ensure humanity's survival.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    "https://youtu.be/2LqzF5WauAw"
)

inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use of dream-sharing "
    "technology, is given the inverse task of planting an idea into "
    "the mind of a CEO.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://youtu.be/8hP9D6kZseM"
)


movies = [hunger_games, catching_fire, mockingjay_part1, mockingjay_part2,
          interstellar, inception]
fresh_tomatoes.open_movies_page(movies)
