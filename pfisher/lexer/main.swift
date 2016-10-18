

import Foundation



func main() {
    let myLexer = Lexer()
    let tokens = myLexer.scan("/Users/pfisher/Dropbox/cloud_repos/compilers_peer_group/lexer/inputFile")
    for token in tokens {
        print("Token Type: \(token.tag); Value: \(token.value!)")
    }
    
    let parser = LLParserOne()
    for (nt, firstSet) in parser.firstSet {
        let symbol = nt
        for terminal in firstSet {
            print("Production: \(symbol.name); First Terminal: \(terminal.value)")
        }
    }
    
    for (nt, followSet) in parser.followSet {
        let production = nt as! NonTerminal
        for member in followSet {
            print("Production: \(production.name); Follow Terminal: \(member.value)")
        }
    }
    
    parser.printParsingTable()
}

main()
