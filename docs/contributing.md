# Contributing Guide

## Protocol for Handling Missing Data Entities

When encountering missing or unmatched entities during a merge request process, adhere to the following protocol:

1. **Verification**:
   - Check the entities' information in the data catalog.
   - Verify if alternate entries exist that might clarify the missing entity.

2. **Documentation**:
   - Provide a detailed query to document unmatched or missing data entities.
   - Ensure the query conforms to the project's style and functional guidelines.

3. **Inclusion in MR**:
   - Include the documentation within the merge request comments or as part of supplementary files.
   
4. **Communication**:
   - Reach out to the relevant data steward if one is assigned.
   - If no data steward is assigned, escalate the matter to the project's maintainer.

### Example Query for Missing Entity

```sql
SELECT entity_id, entity_name
FROM public.entities
WHERE entity_id NOT IN (
  SELECT DISTINCT(entity_id)
  FROM public.related_entities
);
```

This query identifies entities that are not referenced in related entities, indicating unmatched data.

### Note
- Do **not** create placeholders for missing entries.
- Adhere to security and coding standards as outlined.

Following these guidelines ensures consistency and accuracy in handling data entities within our projects.
