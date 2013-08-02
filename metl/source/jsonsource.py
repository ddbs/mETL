
# -*- coding: utf-8 -*-

"""
mETL is a Python tool for do ETL processes with easy config.
Copyright (C) 2013, Bence Faludi (b.faludi@mito.hu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, <see http://www.gnu.org/licenses/>.
"""

import metl.source.base, codecs, demjson, metl.fieldmap

class JSONSource( metl.source.base.FileSource ):

    init = ['rootIterator']

    # void
    def __init__( self, fieldset, rootIterator = None, **kwargs ):

        self.rootIterator = self.setRootIterator( rootIterator )
        super( JSONSource, self ).__init__( fieldset, **kwargs )

    def setRootIterator( self, rootIterator ):

        if rootIterator is not None:
            return rootIterator + '/!'
       
        return '!'

    # list
    def getRecordsList( self ):

        d = demjson.decode( self.file_pointer.read() )
        return metl.fieldmap.FieldMap({ 'root': self.rootIterator }).getValues( d ).get('root')

    # FieldSet
    def getTransformedRecord( self, record ):

        return record
