#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Marco Garcia Baturan
# Fecha:2016/12/2/viernes
# Licencia: GNU-SLUC
"""Algoritmo que devuelve los dos primeros digitos del codigo postal segun provincia espanola.
   Este algoritmo primero inicia la funcion para despues preguntar la provincia escrita correctamente
   en castellano, despues busca en el diccionario interno que porta y que finalmente devuelve por
   la linea de comandos.
   En sucesivos refinamientos se agregaran las variantes toponimas segun lenguaje local.
"""
def CPE():
    # entrada de datos
    provincia = raw_input("Introduzca provincia: ")
    #buscar = provincia
    # declaro un diccionario con provincias
    Diccionario = {"Álava":01,"Albacete":02,"Alicante":03,"Almería":04,"Ávila":05,"Badajoz":06,
                   "Islas Baleares":07,"Barcelona":'08',"Burgos":'09',"Cáceres":10,"Cádiz":11,
                    "Castellón":12,"Ciudad Real":13,"Córdoba":14,"La Coruña":15,"Cuenca":16,
                    "Gerona":17,"Granada":18,"Guadalajara":19,"Guipúzcoa":20,"Huelva":21,"Huesca":21,
                    "Jaén":23,"León":24,"Lérida":25,"La Rioja":26,"Lugo":27,"Madrid":28,"Malaga":29,
                    "Murcia":30,"Navarra":31,"Orense":32,"Astirias":33,"Palencia":34,"Las Palmas":35,
                    "Pontevedra":36,"Salamanca":37,"Santa Cruz de Tenerife":38,"Cantabria":39,
                    "Segovia":40,"Sevilla":41,"Soria":42,"Tarragona":43,"Teruel":44,"Toledo":45,
                    "Valencia":46,"Valladolid":47,"Vizcaya":48,"Zamora":49,"Zaragoza":50,"Ceuta":51,
                    "Melilla":52,}
    # imprimo el codigo postal en base a la provincia introducida
    print Diccionario.get(provincia)
# se llama a la funcion para que trabaje
CPE()