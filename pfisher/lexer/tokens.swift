/* Our language Tokens
 */

import Foundation


enum Tag: String {
    case Identifier = "[a-zP]+"
    case ReservedWord // Keywords == Reserved words
    case Number = "[0-9]+"
    case Relop = "(<|<=|=|==)+"
    case bullshit = "\\s+"
}

class Token: Grammar {
    var tag: Tag!
    init(tag: Tag, value: String){
        self.tag = tag
        super.init()
        self.value = value
    }
}