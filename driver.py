##############################################################################
#
# File:         driver.py
# Date:         Tue 11 Sep 2018  11:33
# Author:       Ken Basye
# Description:  Driver for testing bloxorz algorithms
#
##############################################################################

"""
Driver for testing bloxorz algorithms

"""
import pandas as pd
from bloxorz_problem import BloxorzProblem
from bloxorz import Board
import searchGeneric
import searchBFS
import os
import glob

# import pandas as pd


if __name__ == "__main__":
    board_names = glob.glob("boards/*.blx")
    result_table = {}
    AStarMax = []  #
    BFSMPSMax = []  #
    AStarMPSMax = []  #
    BFSMPSClosedMax = []  #
    AStarMPSClosedMax = []  #
    AStarSolLen = []  #
    BFSSolLen = []  #
    AStarMPSLen = []  #
    AStarExpand = []  #
    BFSExpand = []  #
    AStarMPSExpand = []  #
    result_table['Name'] = board_names

    for board_name in sorted(board_names):
        # print("Loading board file %s" % (board_name,))
        with open(board_name) as file:
            board = Board.read_board(file)
        bp0 = BloxorzProblem(board)
        searcher2 = searchBFS.BFSMultiPruneSearcher(bp0)
        searcher1 = searchGeneric.AStarSearcher(bp0)
        searcher3 = searchGeneric.AStarMultiPruneSearcher(bp0)
        result1 = searcher1.search(90)
        result2 = searcher2.search()
        result3 = searcher3.search()

        AStarMax.append(searcher1.frontier_maxsize)
        BFSMPSMax.append(searcher2.frontier_maxsize)
        AStarMPSMax.append(searcher3.frontier_maxsize)
        BFSMPSClosedMax.append(len(searcher2.closed))
        AStarMPSClosedMax.append(len(searcher3.closed))
        AStarExpand.append(searcher1.num_expanded)
        BFSExpand.append(searcher2.num_expanded)
        AStarMPSExpand.append(searcher3.num_expanded)
        print("%s:" % (board_name,))

        if result1 is None:
            print("         A* no solution!")
            AStarSolLen.append(0)
        else:
            sequence = [arc.action for arc in result1.arcs()]
            AStarSolLen.append(len(sequence))
            print("     A*     solution length: %d expansions:%d" % (
                len(sequence), searcher1.num_expanded))

        if result2 is None:
            print("     BFSMPP no solution!")
            BFSSolLen.append(0)
        else:
            sequence = [arc.action for arc in result2.arcs()]
            BFSSolLen.append(len(sequence))
            print("     BFSMPP solution length: %d expansions:%d" % (
                len(sequence), searcher2.num_expanded))

        if result3 is None:
            print("      A*MPP no solution!")
            AStarMPSLen.append(0)
        else:
            sequence = [arc.action for arc in result3.arcs()]
            AStarMPSLen.append(len(sequence))
            print("     A*MPP  solution length: %d expansions:%d" % (
                len(sequence), searcher3.num_expanded))
    result_table['A*_Sol_Len'] = AStarSolLen
    result_table['A*_Expand'] = AStarExpand
    result_table['A*_FMaxSize'] = AStarMax
    result_table['BFSMPS_Sol_Len'] = BFSSolLen
    result_table['BFSMPS_Expand'] = BFSExpand
    result_table['BFSMPS_FMaxSize'] = BFSMPSMax
    result_table['BFSMPS_Closed_MaxSize'] = BFSMPSClosedMax
    result_table['A*MPS_Sol_Len'] = AStarMPSLen
    result_table['A*MPS_Expand'] = AStarMPSExpand
    result_table['A*MPS_FMaxSize'] = AStarMPSMax
    result_table['A*MPS_Closed_MaxSize'] = AStarMPSClosedMax
    table = pd.DataFrame(result_table)
    new_row = {'Name': 'Avg', 'A*_Expand': table['A*_Expand'].mean(), 'A*_FMaxSize': table['A*_FMaxSize'].mean(),
               'BFSMPS_Expand': table['BFSMPS_Expand'].mean(), 'BFSMPS_FMaxSize:': table['BFSMPS_FMaxSize'].mean(),
               'BFSMPS_Closed_MaxSize': table['BFSMPS_Closed_MaxSize'].mean(),
               'A*MPS_Expand': table['A*MPS_Expand'].mean(), 'A*MPS_FMaxSize': table['A*MPS_FMaxSize'].mean(),
               'A*MPS_Closed_MaxSize': table['A*MPS_Closed_MaxSize'].mean(), 'A*_Sol_Len': 'N/A', 'BFSMPS_Sol_Len': 'N/A',
               'A*MPS_Sol_Len': 'N/A'}
    table.append(new_row, ignore_index=True)
    html = table.to_html(index=False)
    text_file = open('data.html', 'w')
    text_file.write(html)
    text_file.close()

    print()
    print()
