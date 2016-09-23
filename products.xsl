<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="utf-8"/>

    <xsl:template match="/">
        <html>
            <body>
                <h2>Bags</h2>
                <table border="1">
                    <tr bgcolor="#9acd32">
                        <th>Name</th>
                        <th>Price</th>
                        <th>Image</th>
                        <th>Description</th>
                    </tr>
                    <xsl:for-each select="data/bag">
                        <tr>
                            <td>
                                <xsl:value-of select="name/@value"/>
                            </td>
                            <td>
                                <xsl:value-of select="price/@value"/>
                            </td>
                            <img>
                                <td><xsl:value-of select="image/@value"/></td>
                            </img>
                            <td>
                                <xsl:value-of select="description/@value"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>