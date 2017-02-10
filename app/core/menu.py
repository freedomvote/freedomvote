from menus.base import Menu, NavigationNode, Modifier
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class CoreMenu(Menu):

    def get_nodes(self, request):
        nodes   = []
        compare = NavigationNode(_('compare'), reverse('compare'), 1, attr={'priority':1003})
        candidates  = NavigationNode(_('candidates'), reverse('candidates'), 2, attr={'priority':1001})
        parties  = NavigationNode(_('parties_list'), reverse('parties_list'), 3, attr={'priority':1002})
        nodes.append(candidates)
        nodes.append(parties)
        nodes.append(compare)
        return nodes

class CoreModifier(Modifier):

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        return sorted(
            nodes,
            key=lambda n: n.attr.get('priority', 1000)
        )


menu_pool.register_menu(CoreMenu)
menu_pool.register_modifier(CoreModifier)
