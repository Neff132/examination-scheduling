#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This class contains all the tests methods
# It should be runed after any completion of the code

import unittest
from colouring import ColorGraph


class TestInstance(unittest.TestCase):
    """ Test used to test examination_instance script
    """
    pass


class TestGraphicer(unittest.TestCase):
    """ Test used to test graphicer script
    """
    pass


class TestColouring(unittest.TestCase):
    """ Test for testing colouring graph script
    """

    def testBuildRandGraph(self):
        """ We first check that the build graph has the right number of nodes,
        then we compare it with some other to check if it is random
        """
        n = 16
        cgraph = ColorGraph()
        cgraph.build_rand_graph(nb_nodes=n)
        # Verify if we have the right number of nodes
        self.assertEqual(len(cgraph.graph.nodes()), n)
        # We build 10 other graphs and we check how many have the same edges
        nb_same = 0
        for i in range(n):
            cg = ColorGraph()
            cg.build_rand_graph(nb_nodes=n)
            if set(cg.graph.edges()) == set(cgraph.graph.edges()):
                nb_same += 1
        self.assertNotEqual(nb_same, n)

    def testColorGraph(self):
        """ We check if two neighbors don't have the same color
        """
        n = 16
        for i in range(n):
            cgraph = ColorGraph()
            cgraph.build_rand_graph(nb_nodes=n)
            cgraph.color_graph(save=False)
            is_correct = True
            for edge in cgraph.graph.edges():
                if cgraph.colours[edge[0]] == cgraph.colours[edge[1]]:
                    is_correct = False
            self.assertTrue(is_correct)

    def testColorGraphRand(self):
        """ We check if two neighbors don't have the same color for the rand algorithm
        """
        n = 16
        for i in range(n):
            cgraph = ColorGraph()
            cgraph.build_rand_graph(nb_nodes=n)
            cgraph.color_graph_rand_iter(it=10, save=False)
            is_correct = True
            for edge in cgraph.graph.edges():
                if cgraph.colours[edge[0]] == cgraph.colours[edge[1]]:
                    is_correct = False
            self.assertTrue(is_correct)

if __name__ == "__main__":
    unittest.main()