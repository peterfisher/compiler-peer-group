/* Predictive Parser for LL(1) Grammer
 
 */

import Foundation

class LLParserOne {
    
    var firstSet: [Grammar : [Grammar]]
    var followSet: [Grammar : [Grammar]]
    var parsingTable: [NonTerminal: [Terminal: NonTerminal?]]
    
    init() {
        self.firstSet = LLParserOne.getFirstSetforLanguage(productions)
        self.followSet = LLParserOne.getFollowSetforLanguage(allNonTerminals, firstSet: firstSet)
        self.parsingTable = LLParserOne.createParsingTableForSets(firstSet, followSet: followSet)
    }
    
    func printParsingTable() {
        print("PARSING TABLE")
        
        for (production, inputTable) in self.parsingTable {
            for terminal in allTerminals {
                if inputTable[terminal]! != nil {
                    let productionName =  inputTable[terminal]!!.name
                    print("Production: \(production.name); Input Symbol: \(terminal.value), allows production: \(productionName)")
                } else {
                    print("Production: \(production.name); Input Symbol: \(terminal.value), allows production: ERROR")

                }
            }
        }
    }
    
    class func createParsingTableForSets(firstSet: [Grammar : [Grammar]], followSet: [Grammar : [Grammar]]) -> [NonTerminal: [Terminal:NonTerminal?]] {
        var parsingTable = [NonTerminal: [Terminal: NonTerminal?]]()
        
        //Intialize empty parsing table
        for production in productions {
            parsingTable[production] = [Terminal: NonTerminal]()
            for terminal in allTerminals {
                parsingTable[production]!.updateValue(nil, forKey: terminal)
            }
        }
        
        for production in productions {
            
            let firstProductionNonTerminal = production.valueList![0]
            let productionFirstTerminals: [Terminal]? = (firstSet[production]?.filter { $0 is Terminal }) as? [Terminal]
            let productionFollowTerminals: [Terminal] = (followSet[production]?.filter {$0 is Terminal } as! [Terminal])
            
            // For each terminal a in FIRST(A), add A -> α to M[A,a]
            if productionFirstTerminals != nil {
                for terminalSymbol in productionFirstTerminals! {
                    parsingTable[production]![terminalSymbol] = production
                }
            }
            
            //If ε is in FIRST(α), then for each terminal b in FOLLOW(A), add A -> α to M[A,b]. If ε is in FIRST(α) and $ is in FOLLOW(A), add A -> α to M[A,$].
            if firstSet[firstProductionNonTerminal]!.contains(endMarkerTerminal) { // If ε is in FIRST(α)
                // then for each terminal b in FOLLOW(A)
                for terminal in productionFollowTerminals {
                    // add A -> α to M[A,b]
                    parsingTable[production]![terminal] = production
                }
            }
            // If ε is in FIRST(α) and $ is in FOLLOW(A)
            if firstSet[firstProductionNonTerminal] == nil || followSet[firstProductionNonTerminal] == nil {
                continue
            }
            if firstSet[firstProductionNonTerminal]!.contains(endMarkerTerminal) && followSet[firstProductionNonTerminal]!.contains(endMarkerTerminal) {
                // add A -> α to M[A,$].
                parsingTable[production]![endMarkerTerminal] = production
            }
        }
        
        return parsingTable
    }
    
    private class func getFollowSetforLanguage(nonTerminals: [Grammar], firstSet _firstSet: [Grammar: [Grammar]]) -> [Grammar: [Grammar]] {
        var _followSet = [Grammar: [Grammar]]()
        
        
        // Initialize follow set with given nontemrinals
        for nonTerminal in nonTerminals {
            _followSet[nonTerminal] = [Grammar]()
        }
        
        for nonTemrinal in nonTerminals {
            _followSet[nonTemrinal]!.append(endMarkerTerminal)
            let lastSymbol = nonTemrinal.valueList!.last!
            
            if lastSymbol is NonTerminal && nonTemrinal.valueList!.endIndex >= 2 {
                var lastSymbolFirstSet = _firstSet[lastSymbol]!
                if lastSymbolFirstSet.contains(endMarkerTerminal) {
                    let secondToLastSymbol = nonTemrinal.valueList![nonTemrinal.valueList!.endIndex - 1]
                    
                    _followSet[secondToLastSymbol]!.append(endMarkerTerminal)
                    lastSymbolFirstSet.removeAtIndex(lastSymbolFirstSet.indexOf(endMarkerTerminal)!)
                    _followSet[nonTemrinal]!.appendContentsOf(lastSymbolFirstSet)
                } else {
                    _followSet[nonTemrinal]!.appendContentsOf(lastSymbolFirstSet)
                }
            }
            
        }
        
        for production in nonTerminals {
            let lastSymbol = production.valueList!.last

            if lastSymbol is NonTerminal && lastSymbol!.valueList!.contains(endMarkerTerminal) {
                let productionFollowSet = _followSet[production]!
                let secondToLastSymbol = production.valueList![production.valueList!.endIndex - 1]
                _followSet[secondToLastSymbol]!.appendContentsOf(productionFollowSet)
            }
        }
        
        
        
        return _followSet
    }
    
    private class func getFirstSetforLanguage(productions: [Grammar]) -> [Grammar: [Grammar]] {
        
        // Define FIRST(α),where α is any string of grammar symbols, to be the set of terminals that begin strings derived from α.
        var _firstSet = [Grammar: [Grammar]]()
        
        for production in productions {
            for symbol in production.valueList! {
                _firstSet[symbol] = LLParserOne.findAllStartTerminalsForSymbol(symbol)
            }
        }
        
        return _firstSet
    }
    
    private class func findAllStartTerminalsForSymbol(symbol: Grammar) -> [Terminal] {
        var firstTerminals = [Terminal]()
        
        if symbol is Terminal {
            firstTerminals.append(symbol as! Terminal)
        } else if symbol is NonTerminal {
            firstTerminals.append(LLParserOne.findFirstTerminalsForNonterminal(symbol))
        } else if symbol is SymbolList {
            firstTerminals.appendContentsOf(LLParserOne.findAllStartTerminalsForSymbol(symbol))
        }
        
        return firstTerminals
    }
    
    private class func findFirstTerminalsForNonterminal(symbol: Grammar) -> Terminal {
        if symbol is Terminal {
            return symbol as! Terminal
        }
        
        var leftDerivation = symbol.valueList![0]
        
        if leftDerivation is NonTerminal {
            leftDerivation = LLParserOne.findFirstTerminalsForNonterminal(leftDerivation)
        }
        
        return leftDerivation as! Terminal
    }
}
