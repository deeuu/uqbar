from uqbar.graphviz.attributes import Attributes


class GraphAttributes:

    _valid_attributes = frozenset([
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
