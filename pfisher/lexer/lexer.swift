/* Lexer for parsing the following language:
 
 IF statement = 'if'
 ID = [a-z]+
 NUM = [0-9]+
 ASSIGN ='='
 LT ='<'
 LE ='<='
 EQ ='=='
 
 */

import Foundation


class RegexEr {
    static func doesRegexMatchString(regex: String, string: String) -> Bool {
        let regex = try! NSRegularExpression(pattern: regex, options: [])
        let match = regex.matchesInString(string, options: [], range: NSMakeRange(0, string.characters.count))
        
        if match.count > 0 { return true} else { return false}
        
    }
    
    static func isString(ch: String) -> Bool {
        return RegexEr.doesRegexMatchString(Tag.Identifier.rawValue, string: ch)
    }
    
    static func isWhiteSpace(ch: String) -> Bool {
        return RegexEr.doesRegexMatchString(Tag.bullshit.rawValue, string: ch)
    }
    
    static func isRelop(ch: String) -> Bool {
        return RegexEr.doesRegexMatchString(Tag.Relop.rawValue, string: ch)
    }
    
    static func isNumber(ch: String) -> Bool {
        return RegexEr.doesRegexMatchString(Tag.Number.rawValue, string: ch)
    }
}

class Lexer {
    var words: [String: Token]
    var line: Int
    var peek: String? {
        get {
            if self.charIndex >= self.inputText.length {
                return nil
            }
            let char = inputText.substringWithRange(NSRange(location: self.charIndex, length: 1))
            return char
        }
    }
    var inputText: NSString
    var charIndex: Int
    var currentCharacter: String!
    
    init() {
        self.words = [String: Token]()
        self.line = 0
        self.charIndex = 0
        self.inputText = NSString()
        
        // Known reserved words
        let if_keyword = Token(tag: Tag.ReservedWord, value: "If")
        self.add_reserve_word(if_keyword)
    }
    
    func nextCharacter() -> String? {
        if self.charIndex >= inputText.length {
            self.currentCharacter = nil
            return nil
        }
        let char = inputText.substringWithRange(NSRange(location: self.charIndex, length: 1))
        self.currentCharacter = char
        
        self.charIndex += 1
        return char
    }
    
    func add_reserve_word(word: Token) {
        self.words[word.value!] = word
    }
    
    func read_while_tag(tag: Tag) -> String {
        var string = ""
        while true {
            string += self.currentCharacter
            if self.peek == nil {
                break
            } else if RegexEr.doesRegexMatchString(tag.rawValue, string: self.peek!) == false {
                break
            }
            self.nextCharacter()
        }
        return string
    }
    
    func readString() -> Token {
        let string = self.read_while_tag(Tag.Identifier)
        
        // Check if reserved word if so return reserved word
        if let reservedWord = self.words[string] {
            return reservedWord
        }
        
        // return generic ID token
        let idToken = Token(tag: Tag.Identifier, value: string)
        
        return idToken
    }
    
    func readRepl() -> Token {
        let string = self.read_while_tag(Tag.Relop)
        let token = Token(tag: Tag.Relop, value: "")
        
        switch string {
        case "=":
            token.value = "ASSIGN"
        case "<":
            token.value = "LT"
        case "<=":
            token.value = "LE"
        case "==":
            token.value = "EQ"
        default:
            print("Invalid REPL read")
        }
        return token
    }
    
    func readNumber() -> Token {
        let string = self.read_while_tag(Tag.Number)
        
        return Token(tag: Tag.Number, value: string)
    }
    
    func scan(filePath: String) -> [Token] {
        /* Start tokenizing given file
         */
        
        let path = NSURL(fileURLWithPath: filePath)
        var tokens = [Token]() // TODO Convert this eventually to a generator
        
        do {
            self.inputText = try  NSString(contentsOfURL: path, encoding: NSUTF8StringEncoding)
        }
        catch {
            print("Error reading file!")
        }
        
        while true {
            self.nextCharacter()
            
            if self.currentCharacter == nil {                         // Check for EOF
                break
            } else if RegexEr.isWhiteSpace(self.currentCharacter!) { // Check for whitespace
                continue
            } else if RegexEr.isString(self.currentCharacter!) {     // Check for String
                tokens.append(self.readString())
            } else if RegexEr.isRelop(self.currentCharacter) {       // Check for Repl
                tokens.append(self.readRepl())
            } else if RegexEr.isNumber(self.currentCharacter) {      // Check for Number
                tokens.append(self.readNumber())
            }
        }
        return tokens
    }
}

