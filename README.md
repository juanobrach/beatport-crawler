# Beatport Crawler to Firebase
##### Obtener y guardar informacion de tracks en Beatport a Firebase
___

```javascript
{
 "name": "Urban Jungle",
 "key": "A min",
 "artist": "Simon Lunardi",
 "genre": "Deep House",
 "preview": "https://geo-samples.beatport.com/lofi/9440819.LOFI.mp3",
 "cover": "https://geo-media.beatport.com/image_size_hq/95x95/16195288.jpg",
 "track_id": "9440819"
}
```


- Clona el repositorio:
```git clone https://github.com/juanobrach/Beatportcrawl.git```

- Instala scrapy:
```pip install Scrapy```

- Ejecuta el spider:
```scrapy crwal tracks```

Las configuraciones de Firebase se encuentran en ```fbconfig_sample.py``` deberan renombrarlo a ```fbconfig.py ```
