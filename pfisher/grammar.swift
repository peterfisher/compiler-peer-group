/* Grammar defintions, non-ternimals and terminals
 */

import Foundation


func == (lhs: Terminal, rhs: Terminal) -> Bool {
    return lhs.hashValue == rhs.hashValue
}
func == (lhs: NonTerminal, rhs: NonTerminal) -> Bool {
    return lhs.hashValue == rhs.hashValue
}

func == (lhs: Grammar, rhs: Grammar) -> Bool {
    return true
}


class Grammar: Hashable {
    var hashValue: Int {get {return 0}}
    var value: String?
    var valueList: [Grammar]?
    var name: String = ""
}

class Terminal: Grammar {
    var uid: Int
    override var hashValue: Int {
        get {
            return self.uid
        }
    }
    
    init(regex: String, name: String, uid: Int) {
        self.uid = uid
        super.init()
        self.name = name
        self.value = regex
    }
}

class NonTerminal: Grammar {
    let repeating: Bool
    
    override var hashValue: Int {
        get {
            var hash: String = ""
            for term in self.valueList! {
                hash += String(term.hashValue)
            }
            
            return Int(hash)!
        }
    }
    
    init(value: [Grammar], repeating: Bool = false, name: String){
        self.repeating = repeating
        super.init()
        self.name = name
        self.valueList = value
    }
}

class SymbolList: Grammar {
    override var hashValue: Int {
        get {
            var hash = 0
            for term in self.valueList! {
                hash += term.hashValue
            }
            return hash
        }
    }
    
    init(value: [Grammar], name: String){
        super.init()
        self.name = name
        self.valueList = value
    }
}

// Grammar Definition
// === Terminal Definitions ===
let functionStartTerminal = Terminal(regex: "λ", name: "func start symbol", uid: 1)
let lambdaTerminal = Terminal(regex: "lambda", name: "Lambda Start Symbol", uid: 2)
let paranOpenTerminal = Terminal(regex: "(", name: "paranOpen", uid: 3)
let paranCloseTerinal = Terminal(regex: ")", name: "paranclose", uid: 4)
let keywordTerminal = Terminal(regex: "[a-zA-Z-]", name: "keyword", uid: 5)
let commaTerminal = Terminal(regex: ",", name: "comma", uid: 6)
let equalsTerminal = Terminal(regex: "=", name: "equals", uid: 7)
let additionTerminal = Terminal(regex: "+", name: "addition operator", uid: 8)
let subtractionTerminal = Terminal(regex: "-", name: "subtraction operator", uid: 9)

// === Non-Terminal Definitions ===
let functionParameterNonTerminal = NonTerminal(value: [keywordTerminal, commaTerminal], name: "functionParameter") // TODO deal with ending comma

// === Productions ===
let functionLabda = NonTerminal(value: [lambdaTerminal,
    keywordTerminal, paranOpenTerminal, functionParameterNonTerminal, paranCloseTerinal], name: "func")
let functionNormal = NonTerminal(value: [functionStartTerminal,
    keywordTerminal, paranOpenTerminal, functionParameterNonTerminal, paranCloseTerinal], name: "func")
// === All Arrays ===
let productions: [NonTerminal] = [functionLabda, functionNormal]
let allNonTerminals: [NonTerminal] = [functionParameterNonTerminal, functionLabda, functionNormal]
let allTerminals: [Terminal] = [functionStartTerminal,lambdaTerminal,paranOpenTerminal,paranCloseTerinal,keywordTerminal,commaTerminal,equalsTerminal,additionTerminal,subtractionTerminal, endMarkerTerminal]
let allLanguageSymbols = [Grammar]()
allLanguageSymbols.append(allNonTerminals)
allLanguageSymbols.append(allTerminals)

// === Special Grammars ===
let endMarkerTerminal = Terminal(regex: "ε", name: "end marker", uid: 10)
