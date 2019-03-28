def pyMan(movies):
  for movie in movies:
    if isinstance(movie,list):
      for m in movie:
        print(m)
    else:
        print(movie)

pyMan(["a","b","c",["d","e","f","g"]])
