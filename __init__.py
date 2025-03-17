# -*- coding: utf-8 -*-
"""
/***************************************************************************
 changeGpkgPath
 A QGIS plugin to repair GPKG projects

                             -------------------
        begin                : 2020-09-02
        copyright            : (C) 2020 by Christoph Candido
        email                : christoph.candido@gmx.at
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface): 
    from .changeGpkgPath import changeGpkgPath
    return changeGpkgPath(iface)

