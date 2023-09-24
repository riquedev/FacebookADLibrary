from facebook_ad_library.types.ad_bool import AdBool


class UnmaskRemovedContent(AdBool):

    def __repr__(self):
        return f"unmask_removed_content={self.value_str}"
