from uqbar.graphviz.Attributes import Attributes


class GraphAttributes(Attributes):
    """
    Graphviz graph object attributes manifest.

    ::

        >>> import uqbar.graphviz
        >>> attributes = uqbar.graphviz.GraphAttributes(
        ...     fontname='Arial',
        ...     fontcolor='grey50',
        ...     )

    ::

        >>> for item in sorted(attributes.items()):
        ...     item
        ...
        ('fontcolor', <Color 'grey50'>)
        ('fontname', 'Arial')

    """

    _valid_attributes = frozenset([
        'Damping',
        'K',
        'URL',
        'bb',
        'bgcolor',
        'center',
        'charset',
        'clusterrank',
        'colorscheme',
        'comment',
        'compound',
        'concentrate',
        'defaultdist',
        'dim',
        'dimen',
        'diredgeconstraints',
        'dpi',
        'epsilon',
        'esep',
        'fontcolor',
        'fontname',
        'fontnames',
        'fontpath',
        'fontsize',
        'forcedlabels',
        'gradientangle',
        'href',
        'id',
        'imagepath',
        'inputscale',
        'label',
        'label_scheme',
        'labeljust',
        'labelloc',
        'landscape',
        'layerlistsep',
        'layers',
        'layerselect',
        'layersep',
        'layout',
        'levels',
        'levelsgap',
        'lheight',
        'lp',
        'lwidth',
        'margin',
        'maxiter',
        'mclimit',
        'mode',
        'model',
        'mosek',
        'newrank',
        'nodesep',
        'nojustify',
        'normalize',
        'notranslate',
        'nslimit',
        'nslimit1',
        'ordering',
        'orientation',
        'outputorder',
        'overlap',
        'overlap_scaling',
        'overlap_shrink',
        'pack',
        'packmode',
        'pad',
        'page',
        'pagedir',
        'quadtree',
        'quantum',
        'rank',
        'rankdir',
        'ranksep',
        'remincross',
        'repulsiveforce',
        'resolution',
        'root',
        'rotate',
        'rotation',
        'scale',
        'searchsize',
        'sep',
        'showboxes',
        'size',
        'smoothing',
        'sortv',
        'splines',
        'start',
        'style',
        'stylesheet',
        'target',
        'truecolor',
        'viewport',
        'voro_margin',
        'xdotversion',
        'xlabel',
        'xlp',
        ])

    _validator_overrides = {}

    def __init__(self, **kwargs):
        Attributes.__init__(self, **kwargs)