import _plotly_utils.basevalidators


class TitlefontValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='titlefont', parent_name='layout.yaxis', **kwargs
    ):
        super(TitlefontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Titlefont',
            data_docs="""
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The plotly service (at https://plot.ly
                or on-premise) generates images on a server,
                where only a select number of fonts are
                installed and supported. These include *Arial*,
                *Balto*, *Courier New*, *Droid Sans*,, *Droid
                Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                Narrow*, *Raleway*, *Times New Roman*.
            size
""",
            **kwargs
        )