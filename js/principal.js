// Objeto mapa
var mapa = L.map("mapaid", {
  center: [9.99, -83.83],
  zoom: 11.3,
});

// Capa base de OSM
osm = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
});

// Capa base Positron de Carto
positromap = L.tileLayer(
  "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
  {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: "abcd",
    maxZoom: 20,
  }
).addTo(mapa);

// Capa base de ESRI World Imagery
esriworld = L.tileLayer(
  "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
  {
    attribution:
      "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
  }
);

// Capas base
var mapasbase = {
  "OpenStreetMap": osm,
  "Carto Positron": positromap,
  "ESRI WorldImagery": esriworld,
};

// Control de capas
control_capas = L.control
  .layers(mapasbase, null, { collapsed: false })
  .addTo(mapa);

// Capa vectorial de puntos en formato GeoJSON
$.getJSON("Datos/GIS/nacientes.geojson", function (geodata) {
  var capa_nacientes = L.divIcon({
    html: '<i class="fa-solid fa-droplet" style="color: #1368aa;"></i>',
    iconSize: [20, 20], // Dimensiones del ícono
    iconAnchor: [10, 10], // Punto central del ícono
    className: "myDivIcon", // Clase personalizada para más estilos si es necesario
  });

  var capa_nacientes = L.geoJson(geodata, {
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, { icon: capa_nacientes });
    },
    style: function (feature) {
      return { color: "#1368aa", weight: 0.5 };
    },
    onEachFeature: function (feature, layer) {
      var popupText =
        "<strong>Nacientes</strong>: " +
        feature.properties.PUNTO_DE_M +
        "<br>" +
        "<strong>Concentracion de nitratos (mg/L)</strong>: " +
        feature.properties.Nitrato;
      layer.bindPopup(popupText);
    },
  }).addTo(mapa);

  control_capas.addOverlay(capa_nacientes, "Nacientes analizadas");
});

// Capa vectorial de polígonos en formato GeoJSON
$.getJSON("Datos/GIS/recarga_acuifera.geojson", function (geodata) {
  var capa_recarga_acuifera = L.geoJson(geodata, {
    style: function (feature) {
      return { color: "lightblue", weight: 1, fillOpacity: 0.4 };  // Ajuste para polígonos
    },
    onEachFeature: function (feature, layer) {
      var popupText =
        "<strong>Recarga Acuífera</strong>: " + feature.properties.recarg_nac;
      layer.bindPopup(popupText);
    },
  }).addTo(mapa);

  control_capas.addOverlay(capa_recarga_acuifera, "Área de recarga de las nacientes");
});

// Capa vectorial de polígonos en formato GeoJSON
$.getJSON("Datos/GIS/sistemas.geojson", function (geodata) {
  var capa_sistema = L.geoJson(geodata, {
    style: function (feature) {
      return { color: "orange", weight: 1, fillOpacity: 0.3 };  // Ajuste para polígonos
    },
    onEachFeature: function (feature, layer) {
      var popupText =
        "<strong>Sistema</strong>: " + feature.properties.nombre +
        "<br>" +
        "<strong>Observaciones</strong>: " +
        feature.properties.obser;
      layer.bindPopup(popupText);
    },
  }).addTo(mapa);

  control_capas.addOverlay(capa_sistema, "Sistemas - cobertura de las Asadas");
});

//Agregar tilelAyer mapa base desde openstreetmap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapa);

document.getElementById('select-location').addEventListener('change', function (e) {
  let coords = e.target.value.split(",");
  mapa.flyTo(coords, 13);
})

document.getElementById('regresar-coordenada').addEventListener('click', function () {
  // Coordenada específica a la que deseas regresar
  var coordenadaEspecifica = [9.99, -83.83];
  // Nivel de zoom al que deseas regresar
  var nivelZoom = 11.3;

  // Haz que el mapa vuele a la coordenada específica con el nivel de zoom definido
  mapa.flyTo(coordenadaEspecifica, nivelZoom);
});

// Capa de coropletas sistemas con respecto a la cobertura del servicio
$.getJSON('Datos/GIS/area.geojson', function (geojson) {
  var area_coropleta = L.choropleth(geojson, {
    valueProperty: 'area',
    scale: ['lightgreen', 'darkgreen'],
    steps: 7,
    mode: 'q',
    style: {
      color: '#fff',
      weight: 2,
      fillOpacity: 0.5
    },
    onEachFeature: function (feature, layer) {
      layer.bindPopup('Distrito: ' + feature.properties.distrito + '<br>' + 'Código Distrital: ' +
        feature.properties.id_distrito + '<br>' + 'Área en km2: ' + feature.properties.area.toLocaleString())
    }
  }).addTo(mapa);
  control_capas.addOverlay(area_coropleta, 'Zona de estudio de la investigación');

  // Leyenda de la capa de coropletas
  var leyenda = L.control({ position: 'bottomleft' })
  leyenda.onAdd = function (mapa) {
    var div = L.DomUtil.create('div', 'info legend')
    var limits = area_coropleta.options.limits
    var colors = area_coropleta.options.colors
    var labels = []

    // Add min & max
    div.innerHTML = '<div class="labels"><div class="min">' + limits[0] + '</div> \
			<div class="max">' + limits[limits.length - 1] + '</div></div>'

    limits.forEach(function (limit, index) {
      labels.push('<li style="background-color: ' + colors[index] + '"></li>')
    })

    div.innerHTML += '<ul>' + labels.join('') + '</ul>'
    return div
  };

  // Añadir y remover la leyenda basándose en la visibilidad de la capa
  mapa.on('overlayadd', function (eventLayer) {
    if (eventLayer.layer === area_coropleta) {
      leyenda.addTo(mapa);
    }
  });

  mapa.on('overlayremove', function (eventLayer) {
    if (eventLayer.layer === area_coropleta) {
      mapa.removeControl(leyenda);
    }
  });

  leyenda.addTo(mapa)
});

// Control de escala
L.control.scale().addTo(mapa);

// Capa vectorial de puntos en formato GeoJSON
$.getJSON("Datos/GIS/nac_CR.geojson", function (geodata) {
  var nac_cr_icon = L.divIcon({
    html: '<i class="fa-solid fa-droplet" style="color: #1368aa;"></i>',
    iconSize: [20, 20], // Dimensiones del ícono
    iconAnchor: [10, 10], // Punto central del ícono
    className: "myDivIcon", // Clase personalizada para más estilos si es necesario
  });

  var nac_cr = L.geoJson(geodata, {
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, { icon: nac_cr_icon });
    },
    style: function (feature) {
      return { color: "black", weight: 3, fillOpacity: 0.3 };
    },
    onEachFeature: function (feature, layer) {
      var popupText =
        "<strong>Distritos</strong>: " + feature.properties.Distrito_d +
        "<br>" + "<strong>Nombre de la naciente</strong>: " +
        feature.properties.Conocido_c +
        "<br>" + "<strong>Caudadl Autorizado</strong>: " +
        feature.properties.Caudal;
      layer.bindPopup(popupText);
    },
  });

  // Capa de puntos agrupados
  var nac_cr_agrupados = L.markerClusterGroup({
    spiderfyOnMaxZoom: true,
  });
  nac_cr_agrupados.addLayer(nac_cr);

  // Se añade la capa al control de capas pero no al mapa
  control_capas.addOverlay(
    nac_cr_agrupados,
    "Nacientes Registradas por el AYA "
  );

  // Capa de calor (heatmap)
  coordenadas = geodata.features.map((feat) =>
    feat.geometry.coordinates.reverse()
  );
  var nac_cr_calor = L.heatLayer(coordenadas, { radius: 30, blur: 15 });

  // Se añaden la capas al mapa y al control de capas
  control_capas.addOverlay(
    nac_cr_calor,
    "Capa de calor de registros de Asadas del AYA"
  );

// Capa raster modelo digital del terreno
var url_to_geotiff_file = "Datos/GIS/Raster/MDT_wgs84.tif";

fetch(url_to_geotiff_file)
  .then((response) => response.arrayBuffer())
  .then((arrayBuffer) => {
    parseGeoraster(arrayBuffer).then((georaster) => {
      console.log("georaster:", georaster);

      var layer = new GeoRasterLayer({
        georaster: georaster,
        opacity: 0.5,
        pixelValuesToColorFn: function (value) {
          if (value <= 467.073) {
            return "rgba(255, 255, 255, 0.0)";
          } else if (value < 1095.33) {
            return "rgb( 77, 115, 0 )";
          } else if (value < 1533.747) {
            return "rgb( 134, 176, 58 )";
          } else if (value < 1839.688) {
            return "rgb( 206, 237, 157 )";
          } else if (value < 2053.183) {
            return "rgb( 237, 240, 145 )";
          } else if (value < 2359.124) {
            return "rgb( 242, 206, 133 )";
          } else if (value < 2797.54) {
            return "rgb( 199, 145, 55 )";
          } else {
            return "rgb( 156, 91, 0 )";
          }
        },
        resolution: 256, // optional parameter for adjusting display resolution
      });

      // Límites de la capa
      mapa.fitBounds(layer.getBounds());

      // Se agrega la capa raster al control de capas sin activarla
      control_capas.addOverlay(layer, "Modelo Digital del Terreno");

      // Evento onClick
      mapa.on("click", function (event) {
        console.log(event, "event");

        var lat = event.latlng.lat;
        var lng = event.latlng.lng;
        var tmp = geoblaze.identify(georaster, [lng, lat]);

        // Borrar marcadores previos
        mapa.eachLayer(function (layer) {
          if (layer instanceof L.Marker) {
            mapa.removeLayer(layer);
          }

        // Marcador con ventana popup
        marcador = L.marker([lat, lng])
          .addTo(mapa)
          .bindPopup("Altitud: " + Math.round(tmp, 2) + " m.s.n.m<br>Latitud: " + lat.toFixed(5) + "<br>Longitud: " + lng.toFixed(5))
          .openPopup();

        // Eliminar marcador cuando se cierra el popup
        marcador.on("popupclose", function () {
          mapa.removeLayer(marcador);
        });  
      });
    });
  });
})

// Capa WMS de Cobertura de la Tierra
var cobert = L.tileLayer.wms("https://geos1pne.sirefor.go.cr/wms", {
  layers: "cobertura_forestal_2023",
  format: "image/png",
  transparent: true,
});

var legendUrl = "http://geos1pne.sirefor.go.cr/wms?request=GetLegendGraphic&format=image/png&width=20&height=20&layer=cobertura_forestal_2023&";

control_capas.addOverlay(cobert, "Mapa de Bosques y Otras Coberturas de Costa Rica 2023");

cobert.on('load', function () {
    showWmsLegend(legendUrl);
});

function showWmsLegend(uri) {
    L.wmsLegend(uri);
}

// Variable para controlar si la leyenda ya está añadida
var legendAdded = false;
var legendControl = null;  // Variable para almacenar la referencia del control de leyenda

// Función para mostrar o eliminar la leyenda WMS
function showWmsLegend(uri, show) {
    if (show && !legendAdded) {
        // Crear leyenda nueva
        var legend = L.control({ position: 'bottomright' });
        legend.onAdd = function (mapa) {
            var div = L.DomUtil.create('div', 'info legend');
            div.innerHTML = '<img src="' + uri + '" alt="legend">';
            return div;
        };
        legendControl = legend.addTo(mapa);
        legendAdded = true;
    } else if (!show && legendAdded) {
        // Eliminar leyenda existente si es necesario
        mapa.removeControl(legendControl);
        legendAdded = false;
    }
}

// Evento de carga para la capa WMS
cobert.on('load', function () {
    showWmsLegend(legendUrl, mapa.hasLayer(cobert));  // Mostrar leyenda si la capa está activa
});

// Manejar eventos de activación y desactivación de la capa WMS
mapa.on('overlayadd', function (eventLayer) {
    if (eventLayer.layer === cobert) {
        showWmsLegend(legendUrl, true);  // Mostrar leyenda al activar la capa WMS
    }
});

mapa.on('overlayremove', function (eventLayer) {
    if (eventLayer.layer === cobert) {
        showWmsLegend(legendUrl, false);  // Eliminar leyenda al desactivar la capa WMS
    }
});

});