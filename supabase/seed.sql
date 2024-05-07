-- Seed organizations
INSERT INTO organizations (id, name, created_by, deleted, created_at, updated_at)
VALUES 
    ('11116e73-1c03-5de6-9130-5f9925ae8ab4', 'Jem', '{"name": "API", "role": "Admin"}', false, now(), now()),
    ('1087ebe8-1ef8-5d97-8873-735b4949004d', 'Root', '{"name": "API", "role": "Admin"}', false, now(), now());

-- Seed users
INSERT INTO users (id, email, role, organization_id, deleted, created_at, updated_at)
VALUES 
    (gen_random_uuid(), 'moyo@jemhr.com', 'admin', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'john@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'jane@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'michael@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'emily@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'william@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'emma@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'james@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'olivia@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'benjamin@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'isabella@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'daniel@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'sophia@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'david@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'mia@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'joseph@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'charlotte@jemhr.com', 'employee', '11116e73-1c03-5de6-9130-5f9925ae8ab4', false, now(), now()),
    (gen_random_uuid(), 'lebohang@root.com', 'admin', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'chinedu@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'ngozi@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'sibusiso@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'lerato@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'tariq@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'zara@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now()),
    (gen_random_uuid(), 'naledi@root.com', 'employee', '1087ebe8-1ef8-5d97-8873-735b4949004d', false, now(), now());
