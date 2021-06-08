from typing import Optional, Type, TypeVar

TNSObject = TypeVar("TNSObject", bound=NSObject)

class NSObject:
    @classmethod
    def alloc(cls: Type[TNSObject]) -> TNSObject: ...
    def init(self: TNSObject) -> Optional[TNSObject]: ...

class NSDictionary(NSObject): ...
class NSUUID(NSObject): ...
class NSString(NSObject): ...
class NSError(NSObject): ...
class NSData(NSObject): ...
class NSArray(NSObject): ...
class NSNumber(NSValue): ...
class NSValue(NSObject): ...
