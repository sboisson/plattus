# -*- coding: utf-8 -*-

from plattus.flatbuffers.schema import grammar


MONSTER_SCHEMA = """
// example IDL file

namespace MyGame;

attribute "priority";

enum Color : byte { Red = 1, Green, Blue }

union Any { Monster, Weapon, Pickup }

/// This is single struct doc
struct Vec3 {
  x:float;
  y:float;
  z:float;
}

/// This is a
/// multiline table doc
table Monster {
  pos:Vec3;
  mana:short = 150;
  hp:short = 100;
  /// This is single field doc
  name:string;
  friendly:bool = false (deprecated, priority: 1, reason: "this is an attribute value");
  // This is a comment
  inventory:[ubyte];
  color:Color = Blue;
  test:Any;
}

root_type Monster;
"""


def test_grammar_validity():
    grammar.parser.parse(MONSTER_SCHEMA)
